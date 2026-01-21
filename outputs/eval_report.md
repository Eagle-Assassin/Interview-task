# Evaluation Report

## Dataset
- Total evaluated cases: 200

## Priority Metrics
- Accuracy: 0.38
- Macro F1: 0.37

## Action Metrics
- Action accuracy: 0.38

## Priority Confusion Matrix
|           |   Pred_P0 |   Pred_P1 |   Pred_P2 |   Pred_P3 |
|:----------|----------:|----------:|----------:|----------:|
| Actual_P0 |        23 |        10 |         5 |         2 |
| Actual_P1 |        15 |        25 |        16 |         4 |
| Actual_P2 |        11 |        20 |        17 |        12 |
| Actual_P3 |         2 |         6 |        22 |        10 |

## Representative Failure Cases

### Case C-02646
- Gold priority: P2
- Predicted priority: P0
- Gold action: Proceed with standard handling
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 80
- Rationale: This claim presents significant legal risks due to a legal threat escalation and unclear governing law, particularly with cross-border considerations and urgency regarding limitation periods.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-01697
- Gold priority: P2
- Predicted priority: P0
- Gold action: Proceed with standard handling
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim involves a legal dispute with an unclear governing law and a police reference number, indicating potential legal escalation and a significant legal threat.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-09247
- Gold priority: P1
- Predicted priority: P0
- Gold action: Route to legal review
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 90
- Rationale: The claim is at risk due to a legal dispute escalation that involves prior losses and potential fraud indicators, along with urgent time sensitivity in response requirements.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-05609
- Gold priority: P2
- Predicted priority: P0
- Gold action: Proceed with standard handling
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 75
- Rationale: The claim involves a time-sensitive employment dispute with a former contractor, requiring immediate action and a response due to the potential for escalation.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-06138
- Gold priority: P1
- Predicted priority: P0
- Gold action: Route to legal review
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 55
- Rationale: The claim involves an IP infringement allegation with unclear governing law and conflicting information from the client, raising concerns about jurisdictional complexity and the need for clarity on policy application.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-04146
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for coverage review
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 75
- Rationale: The claim involves a legal dispute with a time-sensitive response, indicating a severe legal risk. It also presents jurisdictional complexity due to overseas elements and potential exclusions related to the flood zone.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-09468
- Gold priority: P0
- Predicted priority: P0
- Gold action: Immediate escalation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 90
- Rationale: The claim involves a legal dispute that has escalated into a legal threat with multiple parties, indicating a severe legal risk. Additionally, there is a sense of urgency for responding to the client's concerns.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-09848
- Gold priority: P0
- Predicted priority: P0
- Gold action: Immediate escalation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 60
- Rationale: The claim involves jurisdiction disputes and potential fraud indicators, heightened by cross-border considerations and policy interpretation issues related to a flood zone.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-12663
- Gold priority: P0
- Predicted priority: P0
- Gold action: Immediate escalation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 90
- Rationale: The claim features potential fraud signals due to the suspected duplication of the report and the involvement of police. Additionally, there are overseas elements and policy exclusions that may apply, contributing to jurisdictional complexity.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-14592
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for investigation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 50
- Rationale: This claim involves business interruption due to theft and arson with significant risks related to missing documentation and potential fraud. Additionally, there are cross-border considerations which add to the complexity of the claim.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

