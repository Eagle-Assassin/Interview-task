import logging
from pathlib import Path

import pandas as pd
from sklearn.metrics import f1_score, confusion_matrix

logger = logging.getLogger(__name__)


def evaluation(goldpath: str, output_file: str) -> None:
    logger.info("Starting evaluation step")
    logger.info("Gold file: %s", goldpath)
    logger.info("Prediction output directory: %s", output_file)

    # ------------------------------------------------------------------
    # Load predictions and gold data
    # ------------------------------------------------------------------
    pred_path = Path(output_file) / "predictions.csv"
    pred_df = pd.read_csv(pred_path)
    gold_df = pd.read_csv(goldpath)

    logger.info(
        "Loaded prediction data | rows=%d cols=%d",
        pred_df.shape[0],
        pred_df.shape[1],
    )
    logger.info(
        "Loaded gold data | rows=%d cols=%d",
        gold_df.shape[0],
        gold_df.shape[1],
    )

    # ------------------------------------------------------------------
    # Rename gold columns if required
    # ------------------------------------------------------------------
    gold_df = gold_df.rename(
        columns={
            "expected_priority": "gold_priority",
            "expected_action": "gold_action",
        }
    )

    # ------------------------------------------------------------------
    # Merge predictions with gold labels
    # ------------------------------------------------------------------
    eval_df = pred_df.merge(
        gold_df[["case_id", "gold_priority", "gold_action"]],
        on="case_id",
        how="inner",
    )

    logger.info(
        "Merged prediction & gold datasets | rows=%d",
        len(eval_df),
    )

    # ------------------------------------------------------------------
    # Priority metrics
    # ------------------------------------------------------------------
    priority_accuracy = (
        eval_df["priority"] == eval_df["gold_priority"]
    ).mean()

    priority_f1 = f1_score(
        eval_df["gold_priority"],
        eval_df["priority"],
        labels=["P0", "P1", "P2", "P3"],
        average="macro",
    )

    logger.info(
        "Priority metrics computed | accuracy=%.3f | macro_f1=%.3f",
        priority_accuracy,
        priority_f1,
    )

    # ------------------------------------------------------------------
    # Confusion matrix
    # ------------------------------------------------------------------
    conf_matrix = confusion_matrix(
        eval_df["gold_priority"],
        eval_df["priority"],
        labels=["P0", "P1", "P2", "P3"],
    )

    conf_df = pd.DataFrame(
        conf_matrix,
        index=["Actual_P0", "Actual_P1", "Actual_P2", "Actual_P3"],
        columns=["Pred_P0", "Pred_P1", "Pred_P2", "Pred_P3"],
    )

    logger.debug("Confusion matrix computed")

    # ------------------------------------------------------------------
    # Action accuracy
    # ------------------------------------------------------------------
    action_accuracy = (
        eval_df["recommended_action"] == eval_df["gold_action"]
    ).mean()

    logger.info(
        "Action accuracy computed | accuracy=%.3f",
        action_accuracy,
    )

    # ------------------------------------------------------------------
    # Failure analysis
    # ------------------------------------------------------------------
    failures = eval_df[
        (eval_df["priority"] != eval_df["gold_priority"])
        | (eval_df["recommended_action"] != eval_df["gold_action"])
    ]

    failure_samples = failures.sort_values(
        by="risk_score",
        ascending=False,
    ).head(10)

    logger.info(
        "Failure analysis completed | total_failures=%d | sampled=%d",
        len(failures),
        len(failure_samples),
    )

    # ------------------------------------------------------------------
    # Write evaluation report
    # ------------------------------------------------------------------
    outdir = Path(output_file)
    outdir.mkdir(exist_ok=True)

    report_path = outdir / "eval_report.md"

    with open(report_path, "w") as f:
        f.write("# Evaluation Report\n\n")

        f.write("## Dataset\n")
        f.write(f"- Total evaluated cases: {len(eval_df)}\n\n")

        f.write("## Priority Metrics\n")
        f.write(f"- Accuracy: {priority_accuracy:.2f}\n")
        f.write(f"- Macro F1: {priority_f1:.2f}\n\n")

        f.write("## Action Metrics\n")
        f.write(f"- Action accuracy: {action_accuracy:.2f}\n\n")

        f.write("## Priority Confusion Matrix\n")
        f.write(conf_df.to_markdown())
        f.write("\n\n")

        f.write("## Representative Failure Cases\n\n")

        for _, row in failure_samples.iterrows():
            f.write(f"### Case {row['case_id']}\n")
            f.write(f"- Gold priority: {row['gold_priority']}\n")
            f.write(f"- Predicted priority: {row['priority']}\n")
            f.write(f"- Gold action: {row['gold_action']}\n")
            f.write(f"- Predicted action: {row['recommended_action']}\n")
            f.write(f"- Risk score: {row['risk_score']}\n")
            f.write(f"- Confidence: {row['confidence']}\n")
            f.write(f"- Rationale: {row['rationale']}\n")
            f.write(
                "- Commentary: The model likely under- or over-estimated risk due to "
                "limited, ambiguous, or conflicting signals in the input.\n\n"
            )

    logger.info("Evaluation report written successfully to %s", report_path)
