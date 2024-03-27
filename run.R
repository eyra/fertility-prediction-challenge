#!/usr/bin/env Rscript

# This script calls submission.R. 
# Add your method there.

# To test your submission use the following command: 
# Rscript run.R PreFer_fake_data.csv PreFer_fake_background_data.csv

# Install required packages with Rscript packages.R

library(dplyr)
library(tidyr)


source("submission.R")

print_usage <- function() {
  cat("Usage:\n")
  cat("  Rscript script.R DATA_FILE BACKGROUND_DATA_FILE [--output OUTPUT_FILE]\n")
}

parse_arguments <- function() {
  args <- list()
  command_args <- commandArgs(trailingOnly = TRUE)
  if (length(command_args) < 2) {
    return(args)
  }    
    
  args$data <- commandArgs(trailingOnly = TRUE)[1]
  args$background_data <- commandArgs(trailingOnly = TRUE)[2]
  args$output <- get_argument("--output")
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
  if (is.null(args$data)||is.null(args$background_data)) {
    stop("Error: Please provide data and background_data argument for prediction.")
  }
  
  cat("Processing input data for prediction from:", args$data, " ", args$background_data, "\n")
  if (!is.null(args$output)) {
    cat("Output will be saved to:", args$output, "\n")
  }
  run_predict(args$data, args$background_data, args$output)
}

run_predict <- function(data_path, background_data_path, output=NULL) {
  if (is.null(output)) {
    output <- stdout()
  }
  df <- read.csv(data_path, encoding="latin1")
  background_df <- read.csv(background_data_path, encoding="latin1")
  
  predictions <- predict_outcomes(df, background_df)
  
  # Check if predictions have the required format
  stopifnot(ncol(predictions) == 2,
            all(c("nomem_encr", "prediction") %in% colnames(predictions)))
  
  # Write predictions to output file
  write.csv(predictions, output, row.names = FALSE)
}


# Main function
main <- function() {
  args <- parse_arguments()
  
  parse_and_run_predict(args)
}

# Call main function
main()
