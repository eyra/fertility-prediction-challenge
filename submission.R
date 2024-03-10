# edit the preprocessing function using the code you used for preprocesing the train data 
clean_df <- function(df){
    # Process the input data to feed the model

    ## Selecting variables
    keepcols = c('nomem_encr', 'birthyear_bg', 'gender_bg', 'burgstat_2020','oplmet_2020', 'cf20m454')      
    
    df <- df %>% select(all_of(keepcols))

    # imputing missing values with mode (for factors) or median (for interval variables)
    my_mode <- function(x) {
    x <-x[!is.na(x)]
    ux <- unique(x)
    tab <- tabulate(match(x, ux))
    mode <- ux[tab == max(tab)]
    ifelse(length(mode) > 1, sample(mode, 1), mode)
    }
    
    df <- df %>% 
      mutate(across(c(gender_bg, burgstat_2020, oplmet_2020, cf20m454), ~replace_na(., my_mode(.))), 
             across(c(gender_bg, burgstat_2020, oplmet_2020, cf20m454), as.factor),
             across(birthyear_bg, ~replace_na(., median(., na.rm=TRUE)))) 
   
    return(df)
}



# if necessary, edit the function so it returns predicted classes (1/0), not probabilities
predict_outcomes <- function(df, model_path="./model.rds"){
  # preprocess the holdout data
  df <- clean_df(df)
  ids <- select(df, nomem_encr)
  
  # Load the model
  model <- readRDS(model_path)
  
  # !if necessary, make edits to produce predicted classes
  # E.g. if you used glm() function to train a model, add 'type="response"' to get probabilities 
  pred <- predict(model, df, type="response") 
  #and then transform them into predicted classes
  pred <- ifelse(pred>0.5, 1, 0)  
  
  # adding prediction column to id column
  ids$prediction<- pred  
  
  return(ids)
}


# ######## do not edit this ############################
# df <- read.csv(args[1])
# predictions <- predict_holdout(df)
# write.csv(predictions,"predictions.csv", row.names = FALSE)
