# This is an example script to train your model given the (cleaned) input dataset.
# 
# This script will not be run on the holdout data, 
# but the resulting model model.joblib will be applied to the holdout data.
# 
# It is important to document your training steps here, including seed, 
# number of folds, model, et cetera

train_save_model <- function(clean_df) {
  # Trains a model using the cleaned dataframe and saves the model to a file.

  # Parameters:
  # cleaned_df (dataframe): The cleaned data from clean_df function to be used for training the model.

  ## This script contains a bare minimum working example
  set.seed(1) # not useful here because logistic regression deterministic
  
  # Logistic regression model
  model <- glm(new_child ~ age, family = "binomial", data = clean_df)
  
  # Save the model
  saveRDS(model, "model.rds")
}