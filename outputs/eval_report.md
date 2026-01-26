# Evaluation Report

## Dataset
- Total evaluated cases: 200

## Priority Metrics
- Accuracy: 0.33
- Macro F1: 0.33

## Action Metrics
- Action accuracy: 0.38

## Priority Confusion Matrix
|           |   Pred_P0 |   Pred_P1 |   Pred_P2 |   Pred_P3 |
|:----------|----------:|----------:|----------:|----------:|
| Actual_P0 |        24 |         9 |         6 |         1 |
| Actual_P1 |        24 |        16 |        15 |         5 |
| Actual_P2 |        19 |        13 |        15 |        13 |
| Actual_P3 |         4 |         7 |        18 |        11 |

## Representative Failure Cases

### Case C-02646
- Gold priority: P2
- Predicted priority: P0
- Gold action: Proceed with standard handling
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim involves a legal dispute with potential escalations due to unclear governing law and cross-border elements, raising significant legal risks that require urgent attention.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-03240
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for investigation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 90
- Rationale: The claim involves a fire damage incident at a warehouse with urgent regulatory and police involvement. Potential exclusions could apply, warranting careful review of coverage terms.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-15951
- Gold priority: P3
- Predicted priority: P0
- Gold action: Reject claim
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 45
- Rationale: The claim involves a legal dispute with jurisdictional issues and lacks supporting documentation, increasing the complexity and potential for conflicting information.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-08943
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for investigation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim presents several risk signals including severe regulatory involvement due to fire damage following heavy rainfall, potential fraud indications as the damage report is suspected to be a duplicate, and business-critical impact concerns.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-07881
- Gold priority: P2
- Predicted priority: P0
- Gold action: Route to advisory intake
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim involves potential IP infringement, which carries severe legal risks and has conflicting information associated with it. There is police involvement noted, adding complexity to the case.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-08588
- Gold priority: P1
- Predicted priority: P0
- Gold action: Route to legal review
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim raises severe legal risks due to an IP infringement allegation and a disputed jurisdiction, indicating potential complex legal disputes.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-09247
- Gold priority: P1
- Predicted priority: P0
- Gold action: Route to legal review
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 90
- Rationale: The claim is at risk due to legal dispute escalation with a potential for fraud, as indicated by prior losses and urgency in response required. There may also be policy exclusions that could affect coverage.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-10144
- Gold priority: P0
- Predicted priority: P0
- Gold action: Immediate escalation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 55
- Rationale: The claim involves a class action due to water ingress at commercial premises, indicating significant legal risks and possible coverage interpretation issues.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-09848
- Gold priority: P0
- Predicted priority: P0
- Gold action: Immediate escalation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim involves a formal letter from a counterparty with disputed jurisdiction and indicators of potential fraud, coupled with complex cross-border considerations and possible policy exclusions due to being in a flood zone.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-09468
- Gold priority: P0
- Predicted priority: P0
- Gold action: Immediate escalation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 90
- Rationale: The claim involves a legal threat and a complex incident with multiple parties named, indicating significant legal risks. There is also time sensitivity due to the client's request for an urgent callback.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

