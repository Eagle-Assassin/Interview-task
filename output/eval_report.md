# Evaluation Report

## Dataset
- Total evaluated cases: 200

## Priority Metrics
- Accuracy: 0.34
- Macro F1: 0.34

## Action Metrics
- Action accuracy: 0.29

## Priority Confusion Matrix
|           |   Pred_P0 |   Pred_P1 |   Pred_P2 |   Pred_P3 |
|:----------|----------:|----------:|----------:|----------:|
| Actual_P0 |        26 |        11 |         3 |         0 |
| Actual_P1 |        32 |        11 |        16 |         1 |
| Actual_P2 |        24 |        13 |        19 |         4 |
| Actual_P3 |         6 |         7 |        15 |        12 |

## Representative Failure Cases
### Case C-00724
- Gold priority: P2
- Predicted priority: P0
- Gold action: Proceed with standard handling
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 75
- Rationale: test
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-04003
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for investigation
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 75
- Rationale: test
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-04216
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for investigation
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 75
- Rationale: test
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-04146
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for coverage review
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 75
- Rationale: test
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-03208
- Gold priority: P1
- Predicted priority: P0
- Gold action: Route to legal review
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 65
- Rationale: test
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-02646
- Gold priority: P2
- Predicted priority: P0
- Gold action: Proceed with standard handling
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 50
- Rationale: test
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-02467
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for coverage review
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 60
- Rationale: test
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-01697
- Gold priority: P2
- Predicted priority: P0
- Gold action: Proceed with standard handling
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 45
- Rationale: test
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-11306
- Gold priority: P1
- Predicted priority: P0
- Gold action: Route to legal review
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 60
- Rationale: test
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-14778
- Gold priority: P2
- Predicted priority: P0
- Gold action: Request further information
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 40
- Rationale: test
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

