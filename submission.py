"""
This is an example script to generate the outcome variable given the input dataset.

This script should be modified to prepare your own submission that predicts 
the outcome for the benchmark challenge by changing the predict_outcomes function.

The predict_outcomes function takes a Pandas data frame. The return value must
be a data frame with two columns: nomem_encr and outcome. The nomem_encr column
should contain the nomem_encr column from the input data frame. The outcome
column should contain the predicted outcome for each nomem_encr. The outcome
should be 0 (no child) or 1 (having a child).

clean_df can be used to clean (preprocess) the data.

run.py can be used to test your submission.
"""

import os
import pandas as pd
from joblib import load


def clean_df(df):
    """Process the input data to feed the model."""
    ### If no cleaning is done (e.g. if all the cleaning is done in a pipeline) leave only the "return df" command

    # e.g. keep some variables (the ones you used in your model)
    # keepcols = [
    #     "burgstat2019",
    #     "leeftijd2019",
    #     "woonvorm2019",
    #     "oplmet2019",
    #     "aantalki2019",
    # ]
    # df = df.loc[:, keepcols]

    return df


def predict_outcomes(df):
    """Process the input data and write the predictions."""

    # The predict_outcomes function accepts a Pandas DataFrame as an argument
    # and returns a new DataFrame with two columns: nomem_encr and
    # prediction. The nomem_encr column in the new DataFrame replicates the
    # corresponding column from the input DataFrame. The prediction
    # column contains predictions for each corresponding nomem_encr. Each
    # prediction is represented as a binary value: '0' indicates that the
    # individual did not have a child during 2021-2023, while '1' implies that
    # they did.

    # Keep
    keepcols = [
        "burgstat2019",
        "leeftijd2019",
        "woonvorm2019",
        "oplmet2019",
        "aantalki2019",
    ]
    nomem_encr = df["nomem_encr"]

    df = df.loc[:, keepcols]

    # Load your trained model from the models directory
    model_path = os.path.join(os.path.dirname(__file__), "models", "model.joblib")
    model = load(model_path)

    # Use your trained model for prediction
    predictions = model.predict(df)
    # Return the result as a Pandas DataFrame with the columns "nomem_encr" and "prediction"
    return pd.concat([nomem_encr, pd.Series(predictions, name="prediction")], axis=1)
