# Evaluation Report

## Dataset
- Total evaluated cases: 200

## Priority Metrics
- Accuracy: 0.39
- Macro F1: 0.39

## Action Metrics
- Action accuracy: 0.36

## Priority Confusion Matrix
|           |   Pred_P0 |   Pred_P1 |   Pred_P2 |   Pred_P3 |
|:----------|----------:|----------:|----------:|----------:|
| Actual_P0 |        23 |        10 |         6 |         1 |
| Actual_P1 |        17 |        24 |        16 |         3 |
| Actual_P2 |        11 |        19 |        17 |        13 |
| Actual_P3 |         2 |        10 |        15 |        13 |

## Representative Failure Cases

### Case C-02646
- Gold priority: P2
- Predicted priority: P0
- Gold action: Proceed with standard handling
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 80
- Rationale: This claim involves a legal dispute with unclear governing law and cross-border elements, raising severe legal risks and time sensitivity concerns.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-02467
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for coverage review
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 70
- Rationale: The claim involves a legal dispute with jurisdiction complexity and escalating legal threats, indicating a severe legal risk. Additionally, there are conflicting details regarding policy interpretation and potential exclusions related to flood zone coverage.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-01697
- Gold priority: P2
- Predicted priority: P0
- Gold action: Proceed with standard handling
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 80
- Rationale: This claim presents severe legal risks due to a dispute escalating to legal threats and unclear governing law, with potential involvement of police. Additionally, there are cross-border elements that complicate the jurisdiction.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-08943
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for investigation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim involves severe damage due to heavy rainfall and fire, with regulatory involvement and suspected duplication, indicating potential for fraud. There are concerns about policy exclusions related to the nature of the damage.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-05609
- Gold priority: P2
- Predicted priority: P0
- Gold action: Proceed with standard handling
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 90
- Rationale: The claim involves an employment dispute with time-sensitive response requirements, indicating a severe legal risk. Follow-up actions are necessary to address this matter appropriately.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-06138
- Gold priority: P1
- Predicted priority: P0
- Gold action: Route to legal review
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 45
- Rationale: The claim presents significant risks due to conflicting information, unclear governing law, and cross-border elements, which may lead to legal disputes. Additionally, the handler noted missing documentation and considerations surrounding limitation periods.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-03240
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for investigation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 90
- Rationale: The claim involves significant fire damage to a warehouse and has regulatory involvement, indicating potential legal risks, along with some uncertainty regarding coverage exclusions.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-09848
- Gold priority: P0
- Predicted priority: P0
- Gold action: Immediate escalation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim involves a legal dispute with jurisdiction in question, crossing border considerations, and potential fraud indicators due to police reference. Additionally, there may be policy interpretation issues and exclusions related to the flood zone.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-09247
- Gold priority: P1
- Predicted priority: P0
- Gold action: Route to legal review
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 90
- Rationale: The claim is at risk due to a legal dispute and potential fraud indicators, requiring urgent attention to adhere to limitation periods.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-11306
- Gold priority: P1
- Predicted priority: P0
- Gold action: Route to legal review
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 65
- Rationale: The claim presents significant legal risks due to unclear governing law and potential breach of contract related to IP infringement, raising concerns about jurisdictional complexities.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

