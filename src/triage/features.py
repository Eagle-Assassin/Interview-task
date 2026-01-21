import logging
import pandas as pd

logger = logging.getLogger(__name__)


def process_features():
    logger.info("Starting feature processing step")

    # Load the pre-processed data
    records_copy = pd.read_csv("data/pre-processeddata/preprocessed_data.csv")
    logger.info(
        "Pre-processed records loaded | rows=%d",
        len(records_copy),
    )

    # Initialise an empty dataframe for all LLM signals
    COLUMNS = [
        "case_id",
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
        "mentions_fraud_or_arson",
        "risk_summary",
    ]

    df_all_signals = pd.DataFrame(columns=COLUMNS)
    logger.debug("Initialized empty LLM signal dataframe")

    # Load all LLM output CSVs and merge
    num_batches = (len(records_copy) // 500) + 2
    logger.info("Expecting %d LLM output batches", num_batches - 1)

    for i in range(1, num_batches):
        llm_path = f"data/llmdata/llm_out{i}.csv"
        logger.debug("Loading LLM output file: %s", llm_path)

        df = pd.read_csv(llm_path)
        df_all_signals = pd.concat(
            [df_all_signals, df],
            ignore_index=True,
        )

        logger.debug(
            "LLM batch %d loaded | rows added=%d | total_rows=%d",
            i,
            len(df),
            len(df_all_signals),
        )

    logger.info(
        "All LLM outputs merged into single dataframe | total_rows=%d",
        len(df_all_signals),
    )

    # Merge base dataset with LLM signals
    processed_df = pd.merge(
        records_copy,
        df_all_signals,
        on="case_id",
        how="left",
    )

    logger.info(
        "Base data merged with LLM signals | final_rows=%d | final_cols=%d",
        processed_df.shape[0],
        processed_df.shape[1],
    )

    # Save the processed data
    output_path = "data/processeddata/processeddf.csv"
    processed_df.to_csv(output_path, index=False)

    logger.info("Processed dataset saved successfully at %s", output_path)
