import pandas as pd
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from pathlib import Path


def evaluation(goldpath):
    pred_df = pd.read_csv("output/predictions.csv")
    gold_df = pd.read_csv(goldpath)

    # rename gold columns if needed
    gold_df = gold_df.rename(columns={
    "expected_priority": "gold_priority",
    "expected_action": "gold_action"
    })

    #merge the two dataframes
    eval_df = pred_df.merge(
        gold_df[["case_id", "gold_priority", "gold_action"]],
        on="case_id",
        how="inner"
    )
    print("gold dataset and prediction dataset merged successfully")

    #priority accuracy
    priority_accuracy = (
            eval_df["priority"] == eval_df["gold_priority"]).mean()
    

    # Macro F1 Score
    priority_f1 = f1_score(
            eval_df["gold_priority"],
            eval_df["priority"],    
            labels=["P0", "P1", "P2", "P3"],
            average="macro")
    
    #Confusion Matrix
    conf_matrix = confusion_matrix(
            eval_df["gold_priority"],    
            eval_df["priority"],
            labels=["P0", "P1", "P2", "P3"]
            )

    #Convert the confusion matrix to a DataFrame
    conf_df = pd.DataFrame(conf_matrix,index=["Actual_P0", "Actual_P1", "Actual_P2", "Actual_P3"], 
                           columns=["Pred_P0", "Pred_P1", "Pred_P2", "Pred_P3"])
    
    #Action Evaluation
    action_accuracy = (eval_df["recommended_action"] == eval_df["gold_action"]).mean()

    #Failures
    failures = eval_df[(eval_df["priority"] != eval_df["gold_priority"]) |    
                       (eval_df["recommended_action"] != eval_df["gold_action"])]

    #Failures high risk classification (P0 ↔ P2/P3)
    failure_samples = failures.sort_values( by="risk_score", ascending=False).head(10)

    #from pathlib import Path

    outdir = Path("output")
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

        f.write("## Representative Failure Cases\n")

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
                "- Commentary: The model likely under/over-estimated risk due to "
                "limited or ambiguous signals in the input.\n\n"
            )

