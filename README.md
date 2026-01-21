# Case Triage Mini-Pipeline (Python)

## Overview

This project implements a **deterministic, end-to-end insurance claim triage pipeline** designed to assess **risk, urgency, and recommended actions** for incoming cases.

It was built as part of an interview task to demonstrate:
- Robust data ingestion and validation
- Explainable triage logic
- Evaluation against gold labels
- Clean engineering practices (CLI, logging, testing, reproducibility)

The system ingests structured and unstructured case data, extracts risk signals (optionally via LLM), computes a calibrated risk score, assigns priority and actions, and produces evaluation artefacts.

---

## Key Capabilities

- ✅ CSV schema validation & empty-dataset detection  
- ✅ Sensible default handling for missing data  
- ✅ Deterministic risk scoring & explainable triage logic  
- ✅ Priority (P0–P3) & action prediction  
- ✅ Confidence estimation  
- ✅ Gold-set evaluation (accuracy, macro-F1, confusion matrix)  
- ✅ CLI interface (`python -m triage`)  
- ✅ File-based logging (no console spam)  
- ✅ Unit tests with pytest  
- ✅ Python 3.11 compatible  

---

## Project Structure

```
├── src/
│   ├── triage/
│   │   ├── cli.py                    # CLI entry point
│   │   ├── ingest.py                 # CSV schema preprocessing and extract signals using LLM
│   │   ├── validate.py               # Evaluate predictions against gold data and generate performance reports
│   │   ├── features.py               # LLM signal aggregation
│   │   ├── model.py                  # LLM extraction logic
│   │   ├── predict.py                # Risk scoring & triage logic
│   │   ├── logging_config.py         # Centralised logging
│   │   └── __main__.py
│   └── schema/
│       ├── modeloutput.py            # LLM output schema (Pydantic)
│       └── riskcalculatorinput.py
│
├── data/
│   ├── InterviewTask/AI/
│   │   ├── records.csv
│   │   ├── gold_cases.csv
│   │   └── DataDictionary.md
│   ├── llmdata/
│   ├── pre-processeddata/
│   └── processeddata/
│
├── outputs/
│   ├── predictions.csv
│   └── eval_report.md
│
├── logs/
│   └── triage.log
│
├── tests/
│   ├── test_cli.py
│   ├── test_preprocess.py
│   ├── test_risk_evaluator.py
│   └── test_validate_csv.py
│
├── pyproject.toml
└── README.md
```

---

## Setup Instructions

### 1. Create Environment (Recommended)

Using uv (preferred):

```bash
uv venv
source .venv/bin/activate
uv pip install -e .
uv sync
```

---

## Running the Pipeline

### Full End-to-End Run

```bash
python -m triage run \
  --input data/InterviewTask/AI/records.csv \
  --gold data/InterviewTask/AI/gold_cases.csv \
  --outdir outputs
```

---

## Outputs Generated

| File                      | Description                         |
| :------------------------ | :---------------------------------- |
| `outputs/predictions.csv` | Final triage outputs per case       |
| `outputs/eval_report.md`  | Evaluation metrics & error analysis |
| `logs/triage.log`         | Execution logs                      |

---

## Output Schema (predictions.csv)

| Column               | Description                |
| :-------------------- | :------------------------- |
| `case_id`            | Unique case identifier     |
| `priority`           | P0–P3 urgency level        |
| `risk_score`         | Continuous score (0.0–1.0) |
| `recommended_action` | Action enum                |
| `extracted_signals`  | JSON of key risk signals   |
| `confidence`         | Confidence score (0–100)   |
| `rationale`          | 1–2 sentence justification |

---

## Priority Definitions

| Priority | Meaning                                       |
| :------- | :-------------------------------------------- |
| **P0**   | Critical risk – immediate escalation required |
| **P1**   | High risk – specialist or legal review needed |
| **P2**   | Medium risk – standard handling with caution  |
| **P3**   | Low risk – routine processing                 |

---

## Recommended Actions

Examples include:

- Immediate escalation
- Reject claim
- Escalate for investigation
- Route to legal review
- Escalate for coverage review
- Proceed with standard handling
- Request further information

Actions are determined deterministically from risk signals and priority.

---

## Triage Logic (High Level)

### 1. Validation

- Required columns
- Enum constraints
- Empty CSV detection

### 2. Preprocessing

- Missing values filled with sensible defaults
- Boolean normalization
- Data quality checks

### 3. Signal Extraction

- LLM-assisted structured extraction (optional)
- Batch-safe, cached CSV outputs

### 4. Risk Scoring

Weighted combination of:

- Legal/fraud signals
- Operational risk
- Jurisdiction & service line
- Claim value & client segment

Score bounded to [0.0, 1.0]

### 5. Priority & Action Mapping

- Threshold-based priority assignment
- Priority-aware action logic

### 6. Confidence Estimation

- Penalized by missing data & uncertainty flags

---

## Evaluation

Evaluation is run automatically when `--gold` is supplied.

### Metrics Produced

- Priority accuracy
- Macro-F1 score
- Confusion matrix
- Action accuracy
- Representative failure cases with commentary

**Saved to:** `outputs/eval_report.md`

---

## Running Tests

```bash
pytest -v
```

### Test Coverage Includes

- CSV schema & empty dataset validation
- Preprocessing defaults
- Risk scoring logic
- Priority/action correctness
- CLI smoke test

---

## Logging

**Centralised logging via** `logging_config.py`

- Logs written only to file (no console noise)
- Rotating logs (`logs/triage.log`)
- Includes timestamps, module, function, and message

---

## Design Decisions & Trade-offs

### Why deterministic logic?

- Ensures explainability
- Easier to audit and debug
- Suitable as a baseline before ML/LLM escalation

### Why confidence score?

- Enables downstream manual review gating
- Reflects data quality, not just model certainty

### Why optional LLM usage?

- Structured extraction from free text improves signal richness
- Pipeline still functions without LLM dependency

---

## Known Limitations

- LLM outputs depend on prompt quality
- Risk thresholds are heuristically tuned
- No temporal or cross-case learning
- No production monitoring hooks

---

## What I Would Do Next

- Add probability calibration using historical outcomes
- Introduce SHAP-style explanations
- Add FastAPI service (`POST /triage`)
- Add monitoring for drift & low-confidence spikes
- Replace heuristics with trained baseline ML model

---

## How to Present This in Interview

Be ready to discuss:

- Data issues discovered
- Why some failures happen
- How confidence helps operations
- How to productionise safely

---

## Author

**Anoop Krishnan**  
Python • Data Science • AI Engineering