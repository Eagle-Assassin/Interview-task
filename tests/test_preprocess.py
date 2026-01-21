import pandas as pd
from pathlib import Path

from triage.ingest import preprocess_getstructrureddata


def test_preprocess_creates_output(tmp_path, monkeypatch):
    input_csv = tmp_path / "records.csv"

    df = pd.DataFrame([
        {
            "case_id": "C-101",
            "received_at": "2024-01-01T10:00:00",
            "client_segment": None,
            "jurisdiction": None,
            "service_line": None,
            "claim_value_band": None,
            "attachments_present": None,
            "free_text_summary": "Fire damage",
            "handler_notes": "",
            "historical_outcome": None,
        }
    ])

    df.to_csv(input_csv, index=False)

    # Patch output directory
    monkeypatch.chdir(tmp_path)

    preprocess_getstructrureddata(input_csv)

    output_file = Path("data/pre-processeddata/preprocessed_data.csv")
    assert output_file.exists()

    out_df = pd.read_csv(output_file)
    assert out_df.loc[0, "service_line"] == "No data Available"
