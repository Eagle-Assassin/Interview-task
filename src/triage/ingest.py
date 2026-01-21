import pandas as pd
import logging
import warnings
from src.triage.model import GetFromLlm
from pydantic import ValidationError,BaseModel, Field
from src.schema.riskcalculatorinput import YesNo,ClientSegment,Jurisdiction,ServiceLine,HistoricalOutcome,ClaimValueBand

warnings.filterwarnings(
    "ignore",
    message="A value is trying to be set on a copy of a DataFrame",
    category=FutureWarning,
)

logger = logging.getLogger(__name__)

class EmptyDatasetError(ValueError):
    """Raised when input dataset is empty or fully invalid."""
    pass

class ClaimInput(BaseModel):
    case_id: str = Field(
        description="Unique identifier for the claim or case, used for tracking, joins, and auditability."
    )

    client_segment: ClientSegment = Field(
        description="Client size category (SMB, Mid-Market, Enterprise) used to estimate scale of exposure and escalation sensitivity."
    )

    jurisdiction: Jurisdiction = Field(
        description="Primary legal or regulatory jurisdiction governing the claim, influencing regulatory risk and legal complexity."
    )

    service_line: ServiceLine = Field(
        description="Service line responsible for handling the claim (Legal, Insurance, Advisory), used as a risk multiplier."
    )

    claim_value_band: ClaimValueBand = Field(
        description="Estimated financial exposure of the claim expressed as a predefined value band."
    )

    attachments_present: YesNo = Field(
        description="Indicates whether supporting documents or evidence were provided at intake."
    )

    historical_outcome: HistoricalOutcome = Field(
        description="Previously recorded or known outcome of the claim, if available, used only for analysis and calibration."
    )


    free_text_summary : str = Field(
        description="A small description of the case"
    )
    handler_notes : str = Field(
        description="Notes From the handler"
    )
    


def validate_and_clean_csv(input_path: str) -> pd.DataFrame:
    logger.info("Starting CSV validation | path=%s", input_path)

    # ---------- Load ----------
    df = pd.read_csv(input_path)

    if df.empty:
        logger.error("Input CSV is empty | path=%s", input_path)
        raise EmptyDatasetError("Input dataset is empty")

    logger.info("CSV loaded | rows=%d | cols=%d", *df.shape)

    df.drop(["received_at"],axis=1,inplace=True)

    # Normalize missing values
    df["service_line"].fillna("No data Available", inplace=True)
    df["client_segment"].fillna("No data Available", inplace=True)
    df["jurisdiction"].fillna("No data Available", inplace=True)
    df["handler_notes"].fillna("No data Available", inplace=True)
    df["claim_value_band"].fillna("Unknown", inplace=True)
    df["historical_outcome"].fillna("Unknown", inplace=True)
    df["attachments_present"].fillna(False, inplace=True)

    # Drop rows without case_id
    before = len(df)
    df.dropna(subset=["case_id"], inplace=True)
    logger.info(
        "Dropped rows with missing case_id | removed=%d",
        before - len(df),
    )

    # Normalize attachment flag
    df["attachments_present"] = df["attachments_present"].apply(
        lambda x: "Yes" if bool(x) else "No"
    )

    validated_rows = []
    invalid_rows = 0
  

    # ---------- Row validation ----------
    for idx, row in df.iterrows():
        try:
            row = row.to_dict()

            # Normalization
            validated = ClaimInput(**row)
            validated_rows.append(validated.model_dump())

        except ValidationError as e:
            invalid_rows += 1
            logger.error(
                "Row validation failed | row=%d | case_id=%s | errors=%s",
                idx,
                row.get("case_id"),
                e.errors(),
            )

    # ---------- Post-validation empty check ----------
    if not validated_rows:
        logger.critical(
            "All rows invalid | total_rows=%d | invalid_rows=%d",
            len(df),
            invalid_rows,
        )
        raise EmptyDatasetError(
            "All rows failed validation — no data to process"
        )

    clean_df = pd.DataFrame(validated_rows)

    logger.info(
        "Validation complete | valid_rows=%d | invalid_rows=%d",
        len(clean_df),
        invalid_rows,
    )

    print(f"\n Validation check completed, Number of rows omited :-> {invalid_rows+(before - len(df))}")

    return clean_df





def preprocess_getstructrureddata(path: str) -> None:    
    
    logger.info("========== Preprocessing & LLM extraction started ==========")

    # -------------------------------------------------
    # Send the  input records for cleaning
    # -------------------------------------------------

    records=validate_and_clean_csv(path)
    
    # -------------------------------------------------
    # Initialize LLM
    # -------------------------------------------------
    llm = GetFromLlm()
    logger.info("LLM client initialized")

    col_data = []
    batch_index = 0

    # -------------------------------------------------
    # LLM extraction loop
    # -------------------------------------------------
    for i in range(len(records)):
        logger.info(f"Executing row {i}")
        input_data = (
            f"caseid:{records['case_id'].loc[i]}; "
            f"Summary: {records['free_text_summary'].loc[i]}; "
            f"handler_notes: {records['handler_notes'].loc[i]}; "
            f"historical outcome: {records['historical_outcome'].loc[i]}; "
            f"has attachment: {records['attachments_present'].loc[i]}"
        )

        try:
            data = llm.generate_details(input_data)
            col_data.append(data)

            logger.debug(
                "Row %d sent to LLM | case_id=%s",
                i,
                records['case_id'].loc[i],
            )

        except Exception:
            logger.error(
                "LLM extraction failed | row=%d | case_id=%s",
                i,
                records['case_id'].loc[i],
                exc_info=True,
            )
            continue

        # -------------------------------------------------
        # Batch save (every 500 rows or last row)
        # -------------------------------------------------
        if (i % 500 == 0 and i != 0) or (i + 1 == len(records)):
            batch_index += 1

            try:
                df = pd.DataFrame([r.model_dump() for r in col_data])
                output_path = f"data/llmdata/llm_out{batch_index}.csv"
                df.to_csv(output_path, index=False)

                logger.info(
                    "LLM batch saved | batch=%d | rows=%d | path=%s",
                    batch_index,
                    len(df),
                    output_path,
                )

            except Exception:
                logger.error(
                    "Failed to write LLM batch %d to disk",
                    batch_index,
                    exc_info=True,
                )
                raise

            col_data = []
        logger.info(f"row {i} execution completed")

    logger.info("LLM extraction completed successfully")

 
    # Drop unused columns
    df.drop(
        ["free_text_summary", "handler_notes"],
        axis=1,
        inplace=True,
        errors="ignore",
    )

    # -------------------------------------------------
    # Save preprocessed dataset
    # -------------------------------------------------
    output_path = "data/pre-processeddata/preprocessed_data.csv"
    records.to_csv(output_path, index=False)

    logger.info(
        "Preprocessed dataset saved successfully | rows=%d | path=%s",
        len(records),
        output_path,
    )
