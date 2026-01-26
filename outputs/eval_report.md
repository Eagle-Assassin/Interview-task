# Evaluation Report

## Dataset
- Total evaluated cases: 200

## Priority Metrics
- Accuracy: 0.36
- Macro F1: 0.36

## Action Metrics
- Action accuracy: 0.36

## Priority Confusion Matrix
|           |   Pred_P0 |   Pred_P1 |   Pred_P2 |   Pred_P3 |
|:----------|----------:|----------:|----------:|----------:|
| Actual_P0 |        23 |        11 |         6 |         0 |
| Actual_P1 |        19 |        21 |        16 |         4 |
| Actual_P2 |         9 |        20 |        19 |        12 |
| Actual_P3 |         3 |         8 |        20 |         9 |

## Representative Failure Cases

### Case C-02646
- Gold priority: P2
- Predicted priority: P0
- Gold action: Proceed with standard handling
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim presents significant legal risks due to an escalation into legal threats, with unclear governing law and cross-border elements involved, necessitating urgent action.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-09247
- Gold priority: P1
- Predicted priority: P0
- Gold action: Route to legal review
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 90
- Rationale: The claim involves a legal threat with a time-sensitive response required, and it has prior losses which may indicate potential policy exclusions. There are police references mentioned, raising risk regarding the authenticity of the claim.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-10144
- Gold priority: P0
- Predicted priority: P0
- Gold action: Immediate escalation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 55
- Rationale: The incident involves water ingress at a commercial property and has been escalated due to a class action, raising significant legal exposure risks and potential concerns regarding coverage exclusions.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-09848
- Gold priority: P0
- Predicted priority: P0
- Gold action: Immediate escalation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim involves a disputed jurisdiction and cross-border considerations, presenting potential fraud indicators. Additionally, the case may face policy interpretation issues and exclusions related to the flood zone.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-09468
- Gold priority: P0
- Predicted priority: P0
- Gold action: Immediate escalation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 90
- Rationale: The claim involves a legal dispute with multiple parties and a threat of legal action, indicating a severe legal risk. Additionally, there is time sensitivity as the client has requested an urgent callback.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-08588
- Gold priority: P1
- Predicted priority: P0
- Gold action: Route to legal review
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim involves an IP infringement allegation with disputed jurisdiction, indicating severe legal and regulatory risk. The presence of legal disputes and cross-border elements further complicates the case.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-06138
- Gold priority: P1
- Predicted priority: P0
- Gold action: Route to legal review
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 45
- Rationale: The claim involves an IP infringement allegation with unclear governing law and potential cross-border implications. There are conflicting reports from the client and missing documentation that may impact the validity and processing of the claim.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-04146
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for coverage review
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 65
- Rationale: The claim presents a severe legal risk due to an escalating legal threat and is time-sensitive. Additionally, there are jurisdictional complexities with overseas elements and potential policy exclusions related to flood zone 3.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-07881
- Gold priority: P2
- Predicted priority: P0
- Gold action: Route to advisory intake
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 80
- Rationale: This claim involves potential intellectual property infringement and is linked to a police reference, indicating possible legal disputes and regulatory risk. Additionally, there is suspicion of it being a duplicate report, which raises conflicting information concerns.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-14592
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for investigation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 50
- Rationale: The claim presents significant risks due to business interruption from theft and arson, with potential fraud indicators and missing documentation raising concerns about its validity.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

