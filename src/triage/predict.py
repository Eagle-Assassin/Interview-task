import logging
import json
import pandas as pd
from pathlib import Path

from schema.riskcalculatorinput import ClaimInput
from triage.ingest import preprocess_getstructrureddata
from src.triage.model import GetFromLlm
from src.triage.features import process_features
from src.triage.validate import evaluation

logger = logging.getLogger(__name__)


class BaseRiskPriors:
    """
    Explainable rule-based risk engine aligned with synthetic gold triage behaviour.

    TOTAL RISK =
        Core Severity
      + Operational Urgency
      + Contextual Complexity
      + Financial Amplifier
      - Uncertainty Penalty

    Final score is clamped to [0, 1].
    """

    # -----------------------------
    # Normalisation helpers
    # -----------------------------
    YES_NO_MAP = {
        "Yes": 1.0,
        "No": 0.0,
        "No data available": 0.25,
    }


     # -----------------------------
    # Contextual priors
    # -----------------------------
    CLIENT_SEGMENT_RISK = {
        "SMB": 0.15,
        "Mid-Market": 0.30,
        "Enterprise": 0.45,
        "No data Available": 0.25,
    }

    JURISDICTION_RISK = {
        "UK": 0.20,
        "EU": 0.30,
        "US": 0.45,
        "Other": 0.25,
        "No data Available": 0.25,
    }

    SERVICE_LINE_MULTIPLIER = {
        "Legal": 1.30,
        "Insurance": 1.00,
        "Advisory": 0.85,
        "No data Available": 1.00,
    }
    
    CLAIM_VALUE_RISK = {
        "<50k": 0.10,
        "50k-250k": 0.30,
        "250k-1m": 0.60,
        ">1m": 0.90,
        "Unknown": 0.30,
    }

     # -----------------------------
    # Risk signal weights
    # -----------------------------
    CORE_SIGNAL_WEIGHTS = {
        "severe_legal_or_regulatory_risk": 0.22,
        "legal_disputes": 0.18,
        "potential_fraud": 0.18,
        "claim_invalid_or_fraudulent": 0.22,
    }

    OPERATIONAL_SIGNAL_WEIGHTS = {
        "has_regulator_involvement": 0.12,
        "has_cross_border_elements": 0.10,
        "has_time_sensitivity": 0.10,
        "has_missing_documentation": 0.08,
        "mentions_fraud_or_arson": 0.12,
    }

    UNCERTAINTY_SIGNALS = [
        "conflicting_information",
        "unclear_incident_description",
        "coverage_terms_unclear",
        "policy_interpretation_issues",
        "required_conditions_not_met",
    ]


class ClaimTriageEvaluator(BaseRiskPriors):

    # =====================================================
    # Core calculation
    # =====================================================
    def calculate_risk_score(self, row: dict) -> dict:
        logger.debug("Starting risk calculation for case_id=%s", row.get("case_id"))

        # -----------------------------
        # Core Severity
        # -----------------------------
        core_severity = sum(
            self.YES_NO_MAP.get(row.get(col), 0.25) * weight
            for col, weight in self.CORE_SIGNAL_WEIGHTS.items()
        )

        # -----------------------------
        # Operational Urgency
        # -----------------------------
        operational_urgency = sum(
            self.YES_NO_MAP.get(row.get(col), 0.25) * weight
            for col, weight in self.OPERATIONAL_SIGNAL_WEIGHTS.items()
        )

        # -----------------------------
        # Contextual Complexity
        # -----------------------------
        jurisdiction_risk = self.JURISDICTION_RISK.get(
            row.get("jurisdiction"), 0.25
        )
        service_multiplier = self.SERVICE_LINE_MULTIPLIER.get(
            row.get("service_line"), 1.0
        )

        contextual_complexity = min(jurisdiction_risk * service_multiplier, 0.50)

        contextual_complexity += (
            self.CLIENT_SEGMENT_RISK.get(row.get("client_segment"), 0.25) * 0.15
        )

        # -----------------------------
        # Financial Amplifier
        # -----------------------------
        financial_amplifier = (
            self.CLAIM_VALUE_RISK.get(row.get("claim_value_band"), 0.30) * 0.20
        )

        # -----------------------------
        # Uncertainty Penalty
        # -----------------------------
        uncertainty_penalty = sum(
            0.03 for col in self.UNCERTAINTY_SIGNALS
            if row.get(col) == "No data available"
        )

        # -----------------------------
        # Raw + Final Risk
        # -----------------------------
        raw_risk = (
            core_severity
            + operational_urgency
            + contextual_complexity
            + financial_amplifier
            - uncertainty_penalty
        )

        final_risk = round(max(min(raw_risk, 1.0), 0.0), 2)

        logger.debug(
            "Risk computed | raw=%.3f final=%.2f | breakdown=%s",
            raw_risk,
            final_risk,
            json.dumps({
                "core_severity": round(core_severity, 3),
                "operational_urgency": round(operational_urgency, 3),
                "contextual_complexity": round(contextual_complexity, 3),
                "financial_amplifier": round(financial_amplifier, 3),
                "uncertainty_penalty": round(uncertainty_penalty, 3),
            })
        )

        return final_risk

    # -----------------------------------------------------

    def determine_priority(self, risk_score: float) -> str:
        if risk_score >= 0.81:
            priority = "P0"
        elif risk_score >= 0.63:
            priority = "P1"
        elif risk_score >= 0.40:
            priority = "P2"
        else:
            priority = "P3"

        logger.debug("Priority determined: %s", priority)
        return priority

    # -----------------------------------------------------

    def determine_action(self, row: dict, risk_score: float, priority: str) -> str:

        if priority == "P0":
            
            if row["potential_fraud"] == "Yes" or row["mentions_fraud_or_arson"] == "Yes":
                action = "Escalate for investigation"
            else:
                action = "Immediate escalation"

        elif priority == "P1":
            if row["legal_disputes"] == "Yes":
                action = "Route to legal review"
            elif (
                row["policy_interpretation_issues"] == "Yes"
                or row["coverage_terms_unclear"] == "Yes"
            ):
                action = "Escalate for coverage review"
            else:
                action = "Escalate for investigation"

        elif priority == "P2":
            if row["has_missing_documentation"] == "Yes":
                action = "Request further information"
            else:
                action = "Proceed with standard handling"

        else:
            if row["claim_invalid_or_fraudulent"] == "Yes":
                action ="Reject claim"
            elif (row["attachments_present"]=="No") or (row["historical_outcome"]in ["Unknown","Rejected"]):
                action ="Request further information"
            else :
                action = "Proceed with standard handling"             
                
                
        logger.debug("Action determined: %s", action)
        return action

    # -----------------------------------------------------

    def calculate_confidence(self, row: dict) -> int:
        confidence = 90

        for col in self.UNCERTAINTY_SIGNALS:
            if col!="required_conditions_not_met":

                if row[col] != "No":
                    confidence -= 10


        if row["has_missing_documentation"] == "Yes":
            confidence -= 15

        if row["attachments_present"] == "No":
            confidence -= 15

        if row["required_conditions_not_met"] == "No":
            Confidence -= 10
        if row["historical_outcome"] == "Unknown":
            Confidence -= 5
        final_confidence = max(confidence, 30)
        logger.debug("Confidence calculated: %s", final_confidence)
        return final_confidence

    # -----------------------------------------------------

    def build_extracted_signals(self, row: dict) -> str:
        logger.debug("Extracting signals")
        return json.dumps(
            {
                "jurisdiction": row["jurisdiction"],
                "service_line": row["service_line"],
                "claim_value_band": row["claim_value_band"],
                "core_risks": {
                    "legal": row["severe_legal_or_regulatory_risk"],
                    "fraud": row["potential_fraud"],
                    "dispute": row["legal_disputes"],
                },
                "operational_flags": {
                    "regulator": row["has_regulator_involvement"],
                    "cross_border": row["has_cross_border_elements"],
                    "urgent": row["has_time_sensitivity"],
                    "missing_docs": row["has_missing_documentation"],
                },
            }
        )


# =====================================================
# Pipeline
# =====================================================

def run_pipeline(input_path: str, gold_path: str | None, outdir1= "outputs"):

    print("Executing....\n\n Kindly refer logs to track the progress",end="\n")


    logger.info("Starting triage pipeline")

    preprocess_getstructrureddata(input_path)
    process_features()

    logger.info("Processed data loaded")
    processed_df = pd.read_csv("data/processeddata/processeddf.csv")

    evaluator = ClaimTriageEvaluator()
    results = []

    for i, row in processed_df.iterrows():
        logger.debug("Processing row %s (case_id=%s)", i, row["case_id"])

        row_dict = row.to_dict()
        risk_score = evaluator.calculate_risk_score(row_dict)
        priority = evaluator.determine_priority(risk_score)
        action = evaluator.determine_action(row_dict, risk_score, priority)
        confidence = evaluator.calculate_confidence(row_dict)
        extracted_signals = evaluator.build_extracted_signals(row_dict)

        results.append(
            [
                row["case_id"],
                priority,
                risk_score,
                action,
                extracted_signals,
                confidence,
                row["risk_summary"],
            ]
        )

    df_out = pd.DataFrame(
        results,
        columns=[
            "case_id",
            "priority",
            "risk_score",
            "recommended_action",
            "extracted_signals",
            "confidence",
            "rationale",
        ],
    )

    outdir = Path(outdir1)
    outdir.mkdir(parents=True, exist_ok=True)

    output_file = outdir / "predictions.csv"
    df_out.to_csv(output_file, index=False)

    logger.info("Results written to %s", output_file)

    print(f"Execution completed  successfully, Kindly refer the  {outdir1}/predictions.csv for predictions")

    if gold_path:
        logger.info("Running evaluation with gold labels: %s", gold_path)
        evaluation(gold_path, outdir1)
        print(f"Evaluation completed  successfully, Kindly refer the path {outdir1}/eval_report.md for report")
