from triage.predict import ClaimTriageEvaluator


def sample_row():
    return {
        "case_id": "C-900",
        "client_segment": "Enterprise",
        "jurisdiction": "US",
        "service_line": "Legal",
        "claim_value_band": ">1m",
        "attachments_present": "Yes",
        "severe_legal_or_regulatory_risk": "Yes",
        "business_critical_impact": "Yes",
        "potential_fraud": "No",
        "legal_disputes": "Yes",
        "policy_interpretation_issues": "No",
        "jurisdictional_complexity": "Yes",
        "coverage_terms_unclear": "No",
        "exclusions_may_apply": "No",
        "has_regulator_involvement": "Yes",
        "has_cross_border_elements": "Yes",
        "has_time_sensitivity": "Yes",
        "has_missing_documentation": "No",
        "mentions_fraud_or_arson": "No",
        "conflicting_information": "No",
        "unclear_incident_description": "No",
        "required_conditions_not_met": "No",
        "claim_invalid_or_fraudulent": "No",
    }


def test_high_risk_priority_p0():
    evaluator = ClaimTriageEvaluator()
    row = sample_row()

    score = evaluator.calculate_risk_score(row)
    priority = evaluator.determine_priority(score)

    assert score >= 0.85
    assert priority == "P0"


def test_action_immediate_escalation():
    evaluator = ClaimTriageEvaluator()
    row = sample_row()

    score = evaluator.calculate_risk_score(row)
    priority = evaluator.determine_priority(score)
    action = evaluator.determine_action(row, score, priority)

    assert action in {
        "Immediate escalation",
        "Escalate for investigation",
    }
