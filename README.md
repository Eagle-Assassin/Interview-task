# Case Triage Mini-Pipeline (Python)

## Overview

This project implements a **deterministic, end-to-end insurance claim triage pipeline** designed to assess **risk, urgency, and recommended actions** for incoming cases.

It was built as part of an interview task to demonstrate:
- Robust data ingestion and validation
- Explainable triage logic
- Evaluation against gold labels
- Clean engineering practices (CLI, logging, testing, reproducibility)

The system ingests structured and unstructured case data, extracts risk signals  using LLM, computes a calibrated risk score, assigns priority and actions, and produces evaluation artefacts.

---

## Key Capabilities

- ✅ CSV schema validation & empty-dataset detection  
- ✅ Sensible default handling for missing data and generate data report
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
│       └── riskcalculatorinput.py    # Risk calculator schema (Pydantic)
│
├── data/
│   ├── InterviewTask/AI/            # Store the data and task details
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
Please ensure you have a .env file in the project root directory with a valid OpenAI API key before running the pipeline.

```bash
OPENAI_API_KEY=your_openai_api_key_here
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

### What this command does
This command run the **complete insurance claim triage workflow**, including data validation, feature extraction, risk scoring, priority assignment, action recommendation, and evaluation against gold labels.

---

## Step-by-step execution flow

### 1. CSV validation & cleaning

- Validates the input dataset schema and enums
- Checks for empty or invalid datasets
- Normalizes missing values (e.g., client segment, jurisdiction, attachments)

### 2. LLM-based signal extraction

- Sends free-text summaries and handler notes to the LLM
- Extracts structured risk signals (legal risk, fraud indicators, ambiguity, etc.)
- Persists intermediate LLM outputs for traceability

### 3. Feature engineering

- Merges structured input data with extracted LLM signals
- Produces a single processed feature table for scoring

### 4. Risk scoring & triage

- Computes a calibrated risk score (0–1)
- Assigns a priority level (P0–P3)
- Determines the recommended handling action
- Generates confidence and rationale for each decision

### 5. Prediction outputs

- Writes predictions to:
```bash
outputs/predictions.csv
```

### 6. Evaluation against gold data (optional)

- If --gold is provided:
    -   Compares predicted priorities and actions to expected values
    -   Computes accuracy, macro-F1, and confusion matrices
    -   Saves a detailed evaluation report to:
```bash

outputs/eval_report.md

```

## Command-line arguments

| Argument   | Description                                                                         |
| ---------- | ----------------------------------------------------------------------------------- |
| `--input`  | Path to the raw claims CSV file                                                     |
| `--gold`   | *(Optional)* Path to gold labels for evaluation                                     |
| `--outdir` | *(Optional)* Directory where predictions and reports are saved defaulted to outputs |

---

## Outputs Generated

| File / Path                    | Description                                                     |
| :----------------------------- | :-------------------------------------------------------------- |
| `outputs/predictions.csv`      | Final triage results per case (priority, action, risk, etc.)    |
| `outputs/eval_report.md`       | Evaluation metrics, confusion matrix, and failure analysis      |
| `outputs/data_report.md`       | Data quality report (missingness, anomalies, schema issues)     |
| `logs/triage.log`              | Execution logs for validation, LLM calls, and scoring           |


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

## Metrics Produced

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

## Action Framework Derivation & Trade-offs

The action framework used in this system is not arbitrary.
It was systematically derived by studying the gold_results.csv and identifying consistent patterns that led to specific operational actions.

The process followed three deliberate steps:

- Study gold outcomes to understand why specific actions were taken
- Map those actions to observable signals in structured + unstructured data
- Encode the logic deterministically, with LLMs used only for signal extraction—not decision-making

### How Actions Were Derived  

### Step 1: Gold Case Analysis

- Each action in `gold_cases.csv` was analyzed alongside:
  - Risk signals
  - Claim context
  - Free-text summaries
  - Outcomes
- This revealed repeatable patterns linking certain signals to specific actions.


### Step 2: LLM-Assisted Signal Extraction

- LLMs were used only to:
  - Convert free-text summaries,historical_outcomes,attachment_present and handler notes a into structured flags
  - Extract indicators such as fraud mentions, legal risk, ambiguity, urgency, and documentation gaps


### Step 3: Deterministic Rule-Based Action Assignment

- Once signals were extracted, pure deterministic logic was applied to derive:
  - Priority (P0–P3)
  - Recommended action
  - Risk Score
  - confidence
- This ensures:
  - Full explainability
  - Auditability
  - Repeatable outputs
---

## Limitations & Drawbacks of the Current Design

## 1. Rule-Based Logic Is Rigid

### Limitation

The decision logic is based on static, manually encoded rules.

 -  Cannot adapt automatically to:
    -  New claim patterns
    -  Emerging fraud tactics
    -  Shifts in regulatory interpretation

 -  Requires manual updates when business logic evolves

### Impact

  -  Rules may become outdated
  -  Edge cases may be misclassified
  -  Maintenance cost increases over time

## 2. Heavy Dependence on Signal Quality

### Limitation

The system assumes that extracted signals are accurate and complete.

  - If the LLM:
    - Misses a signal
    - Misinterprets ambiguous text
    - Produces "No data available" too often
      - the downstream decision is affected

### Impact
  - Incorrect or missing signals propagate deterministically
  - No learning mechanism to correct mistakes
  - “Garbage in → garbage out” effect

## 3. Limited Generalization Beyond Gold Data

### Limitation

Rules are derived from historical gold cases.
  - Gold data may:
    - Be biased
    - Be incomplete
    - Reflect outdated practices

### Impact

  - Poor generalization to novel claim types
  - New risks may not map cleanly to existing rules
  - System mirrors past decisions, not necessarily optimal ones

## 4. Dependence on LLM-Derived Rule Discovery **(Important)**

### Limitation

Initial rule logic was derived by analyzing gold cases with LLM assistance rather than being authored entirely from first-principles domain expertise

### Impact

  - Rules may reflect historical data bias rather than optimal policy intent
  - Regulatory or business nuances might be underrepresented
  - Requires human review, validation, and ongoing governance to ensure correctness and compliance


---

## Role of LLMs in This System

The system deliberately separates rule derivation from rule execution.

## What the LLM is used for

The LLM is used offline / during design time to:

### 1. Analyze gold cases

  - Study `gold_results.csv`
  - Identify recurring relationships between:
    - Risk signals
    - Claim characteristics
    - Final actions and priorities

### 2. Propose candidate decision rules

  - Suggest mappings such as:
    - “If severe legal risk + high claim value → Immediate escalation”
    - “If missing documentation → Request further information”
  - Help surface implicit heuristics that human reviewers apply but do not explicitly document


### 3. Coding Assistance

The LLM is also used as a development aid, including:
  - Assisting in writing:
    - Python modules
    - Validation logic
    - Rule evaluation code
  - Helping structure:
    - CLI interfaces
    - Logging patterns
    - Test cases
  - Supporting rapid iteration while maintaining clean, deterministic architecture

All generated code is **reviewed, controlled, and executed deterministically**.


## What I Would Do Next

- Introduce a baseline ML model (e.g., Logistic Regression, Gradient Boosting).
- Add FastAPI service (`POST /triage`)
- Add monitoring for drift & low-confidence spikes
- Replace heuristics with trained baseline ML model
- Subject all LLM-proposed rules to human expert review before adoption.

---

## Author

**Anoop Krishnan**  
Python • Data Science • AI Engineering