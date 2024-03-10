"""
This is an example script to generate the outcome variable given the input dataset.

This script should be modified to prepare your own submission that predicts 
the outcome for the benchmark challenge by changing the predict_outcomes function. 

The predict_outcomes function takes a Pandas data frame. The return value must
be a data frame with two columns: nomem_encr and outcome. The nomem_encr column
should contain the nomem_encr column from the input data frame. The outcome
column should contain the predicted outcome for each nomem_encr. The outcome
should be 0 (no child) or 1 (having a child).

The script can be run from the command line using the following command:

python run.py input_path 

An example for the provided test is:

python run.py data/test_data_liss_2_subjects.csv
"""

import os
import pandas as pd
from joblib import load


def clean_df(df):
    """Process the input data to feed the model."""
    ### If no cleaning is done (e.g. if all the cleaning is done in a pipeline) leave only the "return df" command

    # e.g. keep some variables (the ones you used in your model)
    keepcols = [
         'birthyear_bg', 
         'gender_bg', 
         'burgstat_2020',
         'oplmet_2020', 
         'cf20m454']
    
    df = df.loc[:, keepcols]

    return df




def predict_outcomes(df, model_path="model.joblib"):
    """Write the predictions."""

    # The predict_outcomes function accepts a Pandas DataFrame as an argument
    # and returns a new DataFrame with two columns: nomem_encr and
    # prediction. The nomem_encr column in the new DataFrame replicates the
    # corresponding column from the input DataFrame. The prediction
    # column contains predictions for each corresponding nomem_encr. Each
    # prediction is represented as a binary value: '0' indicates that the
    # individual did not have a child during 2020-2022, while '1' implies that
    # they did.

    nomem_encr = df[['nomem_encr']]
    # cleaning 
    df = clean_df(df)

    # Load your trained model 
    #model_path = os.path.join(os.path.dirname(__file__), "model.joblib")
    model = load(model_path)

    # Use your trained model for prediction
    predictions = model.predict(df)
    # Return the result as a Pandas DataFrame with the columns "nomem_encr" and "prediction"
    return pd.concat([nomem_encr, pd.Series(predictions, name="prediction")], axis=1)

