import pandas as pd
import pytest
from pathlib import Path

from triage.ingest import validate_and_clean_csv, EmptyDatasetError


def test_empty_csv(tmp_path):
    csv_path = tmp_path / "empty.csv"
    pd.DataFrame().to_csv(csv_path, index=False)

    with pytest.raises(EmptyDatasetError):
        validate_and_clean_csv(csv_path)


def test_valid_csv_passes(tmp_path):
    df = pd.DataFrame([
        {
            "case_id": "C-001",
            "received_at": "2024-01-01T10:00:00",
            "client_segment": "SMB",
            "jurisdiction": "UK",
            "service_line": "Insurance",
            "claim_value_band": "<50k",
            "attachments_present": True,
            "free_text_summary": "Water damage claim",
            "handler_notes": "",
            "historical_outcome": "Accepted",
        }
    ])

    csv_path = tmp_path / "valid.csv"
    df.to_csv(csv_path, index=False)

    clean_df = validate_and_clean_csv(csv_path)

    assert len(clean_df) == 1
    assert clean_df.iloc[0]["case_id"] == "C-001"


def test_invalid_enum_fails(tmp_path):
    df = pd.DataFrame([
        {
            "case_id": "C-002",
            "received_at": "2024-01-01T10:00:00",
            "client_segment": "INVALID",
            "jurisdiction": "UK",
            "service_line": "Insurance",
            "claim_value_band": "<50k",
            "attachments_present": True,
            "free_text_summary": "Test",
            "handler_notes": "",
            "historical_outcome": "Accepted",
        }
    ])

    csv_path = tmp_path / "bad.csv"
    df.to_csv(csv_path, index=False)

    with pytest.raises(EmptyDatasetError):
        validate_and_clean_csv(csv_path)
