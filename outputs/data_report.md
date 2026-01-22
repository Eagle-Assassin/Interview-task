# Data Quality Report

**Input file:** `data/InterviewTask/AI/test.csv`

## Summary
- Rows loaded: 9
- Rows after case_id filter: 9
- Invalid rows: 2

## Missingness
- **case_id**: 0 (0.0%)
- **received_at**: 0 (0.0%)
- **client_segment**: 0 (0.0%)
- **jurisdiction**: 0 (0.0%)
- **service_line**: 0 (0.0%)
- **claim_value_band**: 0 (0.0%)
- **attachments_present**: 0 (0.0%)
- **free_text_summary**: 0 (0.0%)
- **handler_notes**: 2 (22.2%)
- **historical_outcome**: 0 (0.0%)

## Anomalies
- schema_validation_error: {'type': 'schema_validation_error', 'row_index': 4, 'case_id': 'C-00005', 'errors': [{'type': 'enum', 'loc': ('jurisdiction',), 'msg': "Input should be 'UK', 'US', 'EU', 'Other' or 'No data Available'", 'input': 'test', 'ctx': {'expected': "'UK', 'US', 'EU', 'Other' or 'No data Available'"}, 'url': 'https://errors.pydantic.dev/2.12/v/enum'}]}
- schema_validation_error: {'type': 'schema_validation_error', 'row_index': 7, 'case_id': 'C-00008', 'errors': [{'type': 'enum', 'loc': ('client_segment',), 'msg': "Input should be 'SMB', 'Mid-Market', 'Enterprise' or 'No data Available'", 'input': 'test', 'ctx': {'expected': "'SMB', 'Mid-Market', 'Enterprise' or 'No data Available'"}, 'url': 'https://errors.pydantic.dev/2.12/v/enum'}]}
