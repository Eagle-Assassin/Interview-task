# Evaluation Report

## Dataset
- Total evaluated cases: 200

## Priority Metrics
- Accuracy: 0.41
- Macro F1: 0.41

## Action Metrics
- Action accuracy: 0.43

## Priority Confusion Matrix
|           |   Pred_P0 |   Pred_P1 |   Pred_P2 |   Pred_P3 |
|:----------|----------:|----------:|----------:|----------:|
| Actual_P0 |        25 |         9 |         6 |         0 |
| Actual_P1 |        18 |        25 |        14 |         3 |
| Actual_P2 |        14 |        15 |        17 |        14 |
| Actual_P3 |         5 |         5 |        15 |        15 |

## Representative Failure Cases
### Case C-00724
- Gold priority: P2
- Predicted priority: P0
- Gold action: Proceed with standard handling
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim indicates potential business interruption and legal disputes related to intellectual property infringement, with the basement affected. This suggests significant risk of financial impact.
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-01697
- Gold priority: P2
- Predicted priority: P0
- Gold action: Proceed with standard handling
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 70
- Rationale: The claim involves legal disputes with an unclear governing law, posing severe legal risk and potential indicators of fraud due to police involvement.
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-14592
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for investigation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 50
- Rationale: This claim presents several risk signals including potential business interruption, theft, arson, and missing documentation, alongside complex jurisdictional issues due to cross-border elements.
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-12806
- Gold priority: P2
- Predicted priority: P0
- Gold action: Proceed with standard handling
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim involves an employment dispute with a former contractor, presenting potential fraud risk, jurisdictional complexity, and unclear governing law, with police involvement noted.
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-09247
- Gold priority: P1
- Predicted priority: P0
- Gold action: Route to legal review
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 90
- Rationale: This claim involves a legal threat and necessitates a time-sensitive response, indicating severe legal risk alongside a potential for fraud due to prior losses.
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-09468
- Gold priority: P0
- Predicted priority: P0
- Gold action: Immediate escalation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 90
- Rationale: This claim involves a severe legal dispute with multiple parties and a threat of legal action, indicating significant risk exposure. There are elements of arson mentioned, and the situation appears time-sensitive.
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-08253
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for investigation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim presents severe legal risks due to a reported breach of contract and involves fire damage following heavy rainfall, which raises concerns about policy exclusions related to flood events.
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-07881
- Gold priority: P2
- Predicted priority: P0
- Gold action: Route to advisory intake
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 90
- Rationale: This claim involves potential IP infringement with police involvement, indicating severe legal risk and possible fraudulent activity.
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-09848
- Gold priority: P0
- Predicted priority: P0
- Gold action: Immediate escalation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim presents complex incident details with a disputed jurisdiction and potential cross-border implications. Additionally, there are legal disputes involved, and there are mentions of police reference which may indicate fraudulent aspects.
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

### Case C-08588
- Gold priority: P1
- Predicted priority: P0
- Gold action: Route to legal review
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim involves an IP infringement allegation with disputed jurisdiction, indicating potential legal disputes and regulatory risk, necessitating careful interpretation of applicable laws.
- Commentary: The model likely under/over-estimated risk due to limited or ambiguous signals in the input.

