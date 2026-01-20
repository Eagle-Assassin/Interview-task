from schema.riskcalculatorinput import ClaimInput
import json




#risk mappings
class BaseRiskPriors:
    def __init__(self):
        self.YES_NO_MAP = {"Yes": 1.0,    
                           "No": 0.0,    
                           "No data available": 0.5}
        
        self.CLIENT_SEGMENT_RISK = {"SMB": 0.1,    
                                    "Mid-Market": 0.3,    
                                    "Enterprise": 0.5,    
                                    "No data Available": 0.3 }
        
        self.JURISDICTION_RISK   = {"UK": 0.2,    
                                    "EU": 0.3,      
                                    "US": 0.5,    
                                    "Other": 0.25,    
                                    "No data Available": 0.3 }
        
        self.SERVICE_LINE_MULTIPLIER = {"Legal": 1.3,    
                                        "Insurance": 1.0,    
                                        "Advisory": 0.7,    
                                        "No data Available": 1.0 }
        
        self.CLAIM_VALUE_RISK = {"<50k": 0.1,    
                                 "50k-250k": 0.3,    
                                 "250k-1m": 0.6,    
                                 ">1m": 0.9,    
                                 "Unknown": 0.4 }
        
        self.SIGNAL_WEIGHTS = {"severe_legal_or_regulatory_risk": 0.20,    
                                "business_critical_impact": 0.15,    
                                "potential_fraud": 0.15,
                                "legal_disputes": 0.15,
                                "policy_interpretation_issues": 0.10,
                                "jurisdictional_complexity": 0.10,
                                "coverage_terms_unclear": 0.10,
                                "exclusions_may_apply": 0.05
                                }
        


class ClaimTriageEvaluator(BaseRiskPriors):
    
    def calculate_risk_score(self,row:ClaimInput):

        score = 0.0

        # LLM / signal-based risk
        for col, weight in self.SIGNAL_WEIGHTS.items():
            score += self.YES_NO_MAP[row[col]] * weight

        # Jurisdiction × service line interaction
        base_jur = self.JURISDICTION_RISK[row["jurisdiction"]]
        service_mult = self.SERVICE_LINE_MULTIPLIER[row["service_line"]]
        score += min(base_jur * service_mult, 0.7)

        # Client size & financial exposure
        score += self.CLIENT_SEGMENT_RISK[row["client_segment"]] * 0.10
        score += self.CLAIM_VALUE_RISK[row["claim_value_band"]] * 0.20

        print("Risk calculated Successfully")

        return round(min(score, 1.0), 2)

    def determine_priority(self,risk_score):

        

        if risk_score >= 0.80:
            print("Priority calculated Successfully")
            return "P0"
        elif risk_score >= 0.60:
            print("Priority calculated Successfully")
            return "P1"
        elif risk_score >= 0.40:
            print("Priority calculated Successfully")
            return "P2"
        else:
            print("Priority calculated Successfully")
            return "P3"
    
    def determine_action(self,row, risk_score):

        if row["claim_invalid_or_fraudulent"] == "Yes":
            print("Action is decided")
            return "Reject claim"

        if row["severe_legal_or_regulatory_risk"] == "Yes":
            print("Action is decided")
            return "Immediate escalation"

        if row["legal_disputes"] == "Yes":
            print("Action is decided")
            return "Route to legal review"

        if row["policy_interpretation_issues"] == "Yes" or row["coverage_terms_unclear"] == "Yes":
            print("Action is decided")
            return "Escalate for coverage review"

        if row["potential_fraud"] == "Yes":
            print("Action is decided")
            return "Escalate for investigation"

        if risk_score >= 0.60:
            print("Action is decided")
            return "Proceed with standard handling"
        
        print("Action is decided")
        return "Request further information"
    
    def calculate_confidence(self,row):
        confidence = 90

        uncertainty_flags = [
            "conflicting_information",
            "unclear_incident_description",
            "coverage_terms_unclear"
        ]

        for col in uncertainty_flags:
            if row[col] != "No":
                confidence -= 15

        for col in uncertainty_flags:
            if row[col] != "No data available":
                confidence -= 5

        if row["attachments_present"] is False:
            confidence -= 20

        print("Confidence is calculated")
        return max(confidence, 30)
    
 
    def build_extracted_signals(self,row):
        print("signals are identified")
        return json.dumps({
            "jurisdiction": row["jurisdiction"],
            "service_line": row["service_line"],
            "claim_value_band": row["claim_value_band"],
            "legal_risk": row["severe_legal_or_regulatory_risk"],
            "fraud_risk": row["potential_fraud"]
        })



    
        
