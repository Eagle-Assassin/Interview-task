import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report
from joblib import dump
from joblib import load

CATEGORICAL_COLS = [
    "client_segment",
    "jurisdiction",
    "service_line",
    "claim_value_band"
]

FEATURE_COLS = [
    # Structured metadata
    "client_segment",
    "jurisdiction",
    "service_line",
    "claim_value_band",
    "attachments_present",

    # LLM-derived signals
    "severe_legal_or_regulatory_risk",
    "business_critical_impact",
    "potential_fraud",
    "conflicting_information",
    "complex_incident_details",
    "policy_interpretation_issues",
    "legal_disputes",
    "jurisdictional_complexity",
    "coverage_terms_unclear",
    "exclusions_may_apply",
    "new_or_unusual_claim_type",
    "unclear_incident_description",
    "claim_invalid_or_fraudulent",
    "required_conditions_not_met",
    "has_regulator_involvement",
    "has_cross_border_elements",
    "has_time_sensitivity",
    "has_missing_documentation",
    "mentions_fraud_or_arson"
]

TARGET_COL = "expected_priority"   # P0, P1, P2, P3

YES_NO_MAP = {
    "Yes": 1.0,
    "No": 0.0,
    "No data available": 0.5
}




def rf_model_tofetch_priority():
    processed=pd.read_csv('data/processeddata/processeddf.csv')
    gold_labels=pd.read_csv('data/InterviewTask/AI/gold_cases.csv')
    gold_priority = gold_labels[["case_id", "expected_priority"]]

    merged_df = processed.merge(
    gold_priority,
    on="case_id",
    how="left" )

    # Encode tri-state fields
    for col in merged_df.columns:
        if merged_df[col].dtype == "object" and set(merged_df[col].unique()).issubset(YES_NO_MAP.keys()):
            merged_df[col] = merged_df[col].map(YES_NO_MAP)

    # Encode attachments_present
    merged_df["attachments_present"] = merged_df["attachments_present"].map({"Yes": 1, "No": 0})

    preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1), CATEGORICAL_COLS)
    ],
    remainder="passthrough")


    rf_model = RandomForestClassifier(
    n_estimators=300,
    max_depth=10,
    min_samples_leaf=5,
    class_weight="balanced",
    random_state=42)

    pipeline = Pipeline([
        ("prep", preprocessor),
        ("model", rf_model)
    ])

    X = merged_df[FEATURE_COLS]
    y = merged_df[TARGET_COL]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.10,
        stratify=y,
        random_state=102
    )

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Macro F1:", f1_score(y_test, y_pred, average="macro"))
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    MODEL_PATH = "tests/rf_priority_model.joblib"

    dump(pipeline, MODEL_PATH)

    print(f"Model saved to {MODEL_PATH}")

# rf_model_tofetch_priority()

def use_modelprediction(row):

    # Normalize attachments_present
    if "attachments_present" in row:
        val = str(row["attachments_present"]).strip().lower()
        row["attachments_present"] = 1 if val == "yes" else 0
    row_df = pd.DataFrame([row])[FEATURE_COLS]
    pipeline = load("tests/rf_priority_model.joblib")
    predicted_priority = pipeline.predict(row_df)[0]
    return predicted_priority












