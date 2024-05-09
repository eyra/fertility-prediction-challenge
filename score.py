"""
This script is used to calculate the metrics for the challenge leaderboards.

It can be used with the following command:

python score.py 

For example:

python score.py your_predictions.csv PreFer_train_outcome.csv

Note: The ground truth (outcome) needs to be in a seperate file with two columns (nomem_encr, new_child). 

The predictions need to be in a separate file with two columns (nomem_encr, prediction).

Update from April 30:  
Starting from the second intermediate leaderboard, we use this updated `score.py` script. 
When calculating recall, we now take into account not only the cases when a predicted value was available (i.e., not missing) but all cases in the holdout set. 
Specifically, in the updated script, we divide the number of true positives by the total number of positive cases in the ground truth data 
(i.e., the number of people who actually had a new child), rather than by the sum of true positives and false negatives. 
This change only matters if there are missing values in predictions. 
We made this change to avoid a situation where a model makes very accurate predictions for only a small number of cases 
(where the remaining cases were not predicted because of missing values on predictor variables), 
yet gets the same result as a model that makes similar accurate predictions but for all cases. 
Commented lines of code were part of our original scoring function. 

"""

import sys
import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="Score data.")
# Score subcommand
parser.add_argument("prediction_path", help="Path to predicted outcome CSV file.")
# Score subcommand
parser.add_argument("ground_truth_path", help="Path to ground truth outcome CSV file.")
# Score subcommand
parser.add_argument("--output", help="Path to evaluation score output CSV file.")

args = parser.parse_args()


def score(prediction_path, ground_truth_path, output):
    """Score (evaluate) the predictions and write the metrics.

    This function takes the path to a CSV file containing predicted outcomes and the
    path to a CSV file containing the ground truth outcomes. It calculates the overall
    prediction accuracy, and precision, recall, and F1 score for having a child
    and writes these scores to a new output CSV file.

    This function should not be modified.
    """

    if output is None:
        output = sys.stdout
    # Load predictions and ground truth into dataframes
    predictions_df = pd.read_csv(prediction_path)
    ground_truth_df = pd.read_csv(ground_truth_path)

    # Merge predictions and ground truth on the 'id' column
    merged_df = pd.merge(predictions_df, ground_truth_df, on="nomem_encr", how="right")

    # Calculate accuracy
    accuracy = len(merged_df[merged_df["prediction"] == merged_df["new_child"]]) / len(
        merged_df
    )

    # Calculate true positives and false positives
    true_positives = len(
        merged_df[(merged_df["prediction"] == 1) & (merged_df["new_child"] == 1)]
    )
    false_positives = len(
        merged_df[(merged_df["prediction"] == 1) & (merged_df["new_child"] == 0)]
    )

    # Calculate the actual number of positive instances (N of people who actually had a new child) for calculating recall
    n_all_positive_instances = len(merged_df[merged_df["new_child"] == 1])

    # Calculate precision, recall, and F1 score
    try:
        precision = true_positives / (true_positives + false_positives)
    except ZeroDivisionError:
        precision = 0

    try:
        recall = true_positives / n_all_positive_instances
    except ZeroDivisionError:
        recall = 0

    try:
        f1_score = 2 * (precision * recall) / (precision + recall)
    except ZeroDivisionError:
        f1_score = 0
    # Write metric output to a new CSV file
    metrics_df = pd.DataFrame(
        {
            "accuracy": [accuracy],
            "precision": [precision],
            "recall": [recall],
            "f1_score": [f1_score],
        }
    )
    metrics_df.to_csv(output, index=False)


if __name__ == "__main__":
    args = parser.parse_args()
    score(args.prediction_path, args.ground_truth_path, args.output)
