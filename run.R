#!/usr/bin/env Rscript

library(dplyr)
library(tidyr)


source("submission.R")

print_usage <- function() {
  cat("Usage:\n")
  cat("  Rscript script.R predict INPUT_FILE [--output OUTPUT_FILE]\n")
  cat("  Rscript script.R score --prediction PREDICTION_FILE --ground_truth GROUND_TRUTH_FILE [--output OUTPUT_FILE]\n")
}

parse_arguments <- function() {
  args <- list()
  command_args <- commandArgs(trailingOnly = TRUE)
  if (length(command_args) > 0) {
    args$command <- command_args[1]
    
    if (is.null(args$command)) {
      stop("Error: No command provided.")
    }
    
    if (args$command == "predict") {
      args$input <- commandArgs(trailingOnly = TRUE)[2]
      args$output <- get_argument("--output")
    } else if (args$command == "score") {
      args$prediction <- get_argument("--prediction")
      args$ground_truth <- get_argument("--ground_truth")
      args$output <- get_argument("--output")
    }
  } else {
    stop("Error: No command provided. Run the script with predict or score.")
  }
  
  return(args)
}

get_argument <- function(arg_name) {
  if (arg_name %in% commandArgs(trailingOnly = TRUE)) {
    arg_index <- which(commandArgs(trailingOnly = TRUE) == arg_name)
    if (arg_index < length(commandArgs(trailingOnly = TRUE))) {
      return(commandArgs(trailingOnly = TRUE)[arg_index + 1])
    }
  }
  return(NULL)
}

parse_and_run_predict <- function(args) {
  if (is.null(args$input)) {
    stop("Error: Please provide --input argument for prediction.")
  }
  
  cat("Processing input data for prediction from:", args$input, "\n")
  if (!is.null(args$output)) {
    cat("Output will be saved to:", args$output, "\n")
  }
  run_predict(args$input, args$output)
}

run_score <- function(args) {
  if (is.null(args$prediction) || is.null(args$ground_truth)) {
    stop("Error: Please provide --prediction and --ground_truth arguments for scoring.")
  }
  
  cat("Scoring predictions from:", args$prediction, "\n")
  cat("Ground truth data from:", args$ground_truth, "\n")
  if (!is.null(args$output)) {
    cat("Evaluation score will be saved to:", args$output, "\n")
  }
  # Call your submission function for scoring here
}

run_predict <- function(input_path, output=NULL) {
  if (is.null(output)) {
    output <- stdout()
  }
  
  
  # Read data from input file
  df <- read.csv(input_path, encoding="latin1")
  
  # Clean the data
  df <- clean_df(df)  # Assuming clean_df is a function in the submission package
  
  # Make predictions
  predictions <- predict_outcomes(df)  # Assuming predict_outcomes is a function in the submission package
  
  # Check if predictions have the required format
  stopifnot(ncol(predictions) == 2,
            all(c("nomem_encr", "prediction") %in% colnames(predictions)))
  
  # Write predictions to output file
  write.csv(predictions, output, row.names = FALSE)
}


# Main function
main <- function() {
  args <- parse_arguments()
  
  if (args$command == "predict") {
    parse_and_run_predict(args)
  } else if (args$command == "score") {
    run_score(args)
  } else {
    stop("Error: Invalid command. Use 'predict' or 'score'.")
  }
}

# Call main function
main()
