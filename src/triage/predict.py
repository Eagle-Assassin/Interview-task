from schema.riskcalculatorinput import ClaimInput
import json
import pandas as pd
from pathlib import Path
from src.triage.injest import preprocess_getstructrureddata
from src.triage.model import GetFromLlm
from src.triage.features import process_features
from tests.model_rf import use_modelprediction




class BaseRiskPriors:
    """
    Calibrated priors aligned with synthetic gold behaviour.
    """

    YES_NO_MAP = {
        "Yes": 1.0,
        "No": 0.0,
        "No data available": 0.30,
    }

    CLIENT_SEGMENT_RISK = {
        "SMB": 0.15,
        "Mid-Market": 0.30,
        "Enterprise": 0.50,
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

    # Core legal / fraud risk signals
    CORE_SIGNAL_WEIGHTS = {
        "severe_legal_or_regulatory_risk": 0.22,
        "legal_disputes": 0.18,
        "potential_fraud": 0.18,
        "claim_invalid_or_fraudulent": 0.22,
    }

    # Operational & escalation signals
    OPERATIONAL_SIGNAL_WEIGHTS = {
        "has_regulator_involvement": 0.12,
        "has_cross_border_elements": 0.10,
        "has_time_sensitivity": 0.10,
        "has_missing_documentation": 0.08,
        "mentions_fraud_or_arson": 0.12,
    }

    # Uncertainty / ambiguity signals (penalties)
    UNCERTAINTY_SIGNALS = [
        "conflicting_information",
        "unclear_incident_description",
        "coverage_terms_unclear",
        "policy_interpretation_issues",
        "required_conditions_not_met",
    ]


class ClaimTriageEvaluator(BaseRiskPriors):

    def calculate_risk_score(self, row: dict) -> float:
        score = 0.0

        # 1️⃣ Core legal & fraud risk
        for col, weight in self.CORE_SIGNAL_WEIGHTS.items():
            score += self.YES_NO_MAP.get(row[col], 0.25) * weight

        # 2️⃣ Operational escalation risk
        for col, weight in self.OPERATIONAL_SIGNAL_WEIGHTS.items():
            score += self.YES_NO_MAP.get(row[col], 0.25) * weight

        # 3️⃣ Jurisdiction × service line interaction
        base_jur = self.JURISDICTION_RISK[row["jurisdiction"]]
        service_mult = self.SERVICE_LINE_MULTIPLIER[row["service_line"]]
        score += min(base_jur * service_mult, 0.50)

        # 4️⃣ Client size & financial exposure
        score += self.CLIENT_SEGMENT_RISK[row["client_segment"]] * 0.15
        score += self.CLAIM_VALUE_RISK[row["claim_value_band"]] * 0.20

        # 5️⃣ Uncertainty penalty
        for col in self.UNCERTAINTY_SIGNALS:
            if row[col] == "No data available":
                score -= 0.03

        return round(max(min(score, 1.0), 0.0), 2)

    # -----------------------------------------------------

    def determine_priority(self, risk_score: float) -> str:
        if risk_score >= 0.85:
            return "P0"
        elif risk_score >= 0.65:
            return "P1"
        elif risk_score >= 0.40:
            return "P2"
        else:
            return "P3"

    # -----------------------------------------------------
    def determine_action(self, row: dict, risk_score: float, priority: str) -> str:

        # --- P0: always escalation-oriented ---
        if priority == "P0":
            if row["claim_invalid_or_fraudulent"] == "Yes":
                return "Reject claim"
            if row["potential_fraud"] == "Yes" or row["mentions_fraud_or_arson"] == "Yes":
                return "Escalate for investigation"
            return "Immediate escalation"

        # --- P1: structured escalation ---
        if priority == "P1":
            if row["legal_disputes"] == "Yes":
                return "Route to legal review"
            if row["policy_interpretation_issues"] == "Yes" or row["coverage_terms_unclear"] == "Yes":
                return "Escalate for coverage review"
            return "Escalate for investigation"

        # --- P2: controlled handling ---
        if priority == "P2":
            if row["has_missing_documentation"] == "Yes":
                return "Request further information"
            return "Proceed with standard handling"

        # --- P3: minimal handling ---
        if row["claim_invalid_or_fraudulent"] == "Yes":
            return "Reject claim"

        return "Proceed with standard handling"


    # -----------------------------------------------------

    def calculate_confidence(self, row: dict) -> int:
        confidence = 90

        for col in self.UNCERTAINTY_SIGNALS:
            if row[col] != "No":
                confidence -= 10

        if row["has_missing_documentation"] == "Yes":
            confidence -= 15

        if row["attachments_present"] == "No":
            confidence -= 15

        return max(confidence, 30)

    # -----------------------------------------------------

    def build_extracted_signals(self, row: dict) -> str:
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



def run_pipeline(input_path: str, gold_path: str | None, outdir: str):

    print("Starting triage pipeline...")
 
    #inject the data
    preprocess_getstructrureddata(input_path)
    

    #Analyse  and process the features
    process_features()

    #Predict the output
    #initialize the evaluator object
    claim_calculator=ClaimTriageEvaluator()


    #Initialize output columns
    outcols=['case_id','priority','risk_score','recommended_action','extracted_signals','confidence','rationale']

    #load the processed dataframe
    processed_df=pd.read_csv('data/processeddata/processeddf.csv')

    claim_calculator = ClaimTriageEvaluator()
    results = []

    for i in range(0,len(processed_df)):
        row=processed_df.loc[i].to_dict()
        comment=processed_df['risk_summary'].loc[i]
        case_id=row['case_id']
        risk_score=claim_calculator.calculate_risk_score(row)
        priority=claim_calculator.determine_priority(risk_score)
        # priority = use_modelprediction(row)
        action=claim_calculator.determine_action(row,risk_score,priority)
        confidence=claim_calculator.calculate_confidence(row)
        extracted_signals=claim_calculator.build_extracted_signals(row)
        results.append([case_id,priority,risk_score,action,extracted_signals,confidence,comment])

    df_out=pd.DataFrame(results,columns=outcols)

    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    output_file = outdir / "predictions.csv"
    df_out.to_csv(output_file, index=False)

    print(f"Results written to {output_file}")

    if gold_path:
        print(f"Gold cases provided: {gold_path}")