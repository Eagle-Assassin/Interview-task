# Case Records Data Dictionary

## records.csv

| Column | Type | Description |
|------|------|-------------|
| case_id | string | Unique case identifier |
| received_at | datetime (ISO 8601) | When the case was received |
| client_segment | enum | SMB, Mid-Market, Enterprise |
| jurisdiction | enum | UK, EU, US, Other |
| service_line | enum | Insurance, Legal, Advisory |
| claim_value_band | enum | <50k, 50k-250k, 250k-1m, >1m, Unknown |
| attachments_present | boolean | Whether documents were attached |
| free_text_summary | string | Unstructured description of the case |
| handler_notes | string | Optional internal notes |
| historical_outcome | enum | Accepted, Rejected, Escalated, Settled, Unknown |

Notes:
- free_text_summary may contain inconsistent terminology, missing information, or conflicting signals.
- handler_notes may be empty.
- historical_outcome is only populated for some records and may be used for evaluation.
