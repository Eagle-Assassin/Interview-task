# Evaluation Report

## Dataset
- Total evaluated cases: 200

## Priority Metrics
- Accuracy: 0.36
- Macro F1: 0.36

## Action Metrics
- Action accuracy: 0.40

## Priority Confusion Matrix
|           |   Pred_P0 |   Pred_P1 |   Pred_P2 |   Pred_P3 |
|:----------|----------:|----------:|----------:|----------:|
| Actual_P0 |        24 |         9 |         6 |         1 |
| Actual_P1 |        19 |        23 |        14 |         4 |
| Actual_P2 |        11 |        19 |        16 |        14 |
| Actual_P3 |         3 |         6 |        21 |        10 |

## Representative Failure Cases

### Case C-02646
- Gold priority: P2
- Predicted priority: P0
- Gold action: Proceed with standard handling
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim presents severe legal risks due to a dispute that may escalate to legal actions. Jurisdictional complexities and urgency in addressing limitation periods further heighten the risk.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-02467
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for coverage review
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim involves a legal dispute with escalated threats and jurisdictional issues, indicating severe legal risk. Time sensitivity and unclear coverage due to flood zone implications further complicate the situation.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-05609
- Gold priority: P2
- Predicted priority: P0
- Gold action: Proceed with standard handling
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 90
- Rationale: The claim involves a time-sensitive employment dispute, requiring careful management due to potential legal exposure. A follow-up is needed due to caller uncertainty and to consider limitation periods.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-15951
- Gold priority: P3
- Predicted priority: P0
- Gold action: Reject claim
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 45
- Rationale: The claim involves a legal dispute with jurisdictional complexity and missing documentation, indicating potential severe legal risks. The lack of supporting documentation and unclear jurisdiction raise concerns about compliance and resolution.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-19078
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for investigation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 90
- Rationale: The claim involves severe legal risks due to a class action related to compromised roofing from heavy rainfall, indicating potential regulatory scrutiny. Additionally, there is urgency for client interaction as noted by the request for an urgent callback.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-11306
- Gold priority: P1
- Predicted priority: P0
- Gold action: Route to legal review
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 65
- Rationale: The claim involves a potential breach of contract and IP infringement, raising severe legal risks due to unclear governing law and legal disputes.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-14592
- Gold priority: P1
- Predicted priority: P0
- Gold action: Escalate for investigation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 40
- Rationale: The claim indicates a significant business interruption due to theft and arson, with potential fraudulent activity suggested; however, there is a lack of supporting documentation and unclear incident details, raising concerns about compliance with policy conditions.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-12806
- Gold priority: P2
- Predicted priority: P0
- Gold action: Proceed with standard handling
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 55
- Rationale: The claim involves an employment dispute with potential fraud indicators, unclear governing law, and complex jurisdictional issues. Missing attachments and regulatory involvement add to the risk profile.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-12663
- Gold priority: P0
- Predicted priority: P0
- Gold action: Immediate escalation
- Predicted action: Escalate for investigation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim has potential fraud indicators and conflicting information, particularly with the mention of a duplicate report. Additionally, it involves cross-border elements and may have applicable exclusions.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

### Case C-16335
- Gold priority: P1
- Predicted priority: P0
- Gold action: Route to legal review
- Predicted action: Immediate escalation
- Risk score: 1.0
- Confidence: 80
- Rationale: The claim involves severe legal risk due to a formal letter from a counterparty and an injunction. Additionally, there are complexities related to cross-border elements and the need for expert interpretation.
- Commentary: The model likely under- or over-estimated risk due to limited, ambiguous, or conflicting signals in the input.

