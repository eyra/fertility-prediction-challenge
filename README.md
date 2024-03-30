# Predicting Fertility Data Challenge (PreFer)

This is a template repository to submit your method on the Next platform for phase 1 of the Predicting Fertility Data Challenge ([PreFer](https://preferdatachallenge.nl)). [Here](https://preferdatachallenge.nl/#how-to-participate) you can read how to participate in the challenge. The challenge is to predict whether an individual will have a child within a three year period (2021-2023), based on survey data from previous years (2007-2020). Data come from the [LISS panel](https://www.centerdata.nl/en/liss-panel). For more information, on the data challenge, please visit the [website](https://preferdatachallenge.nl) and read [this paper](https://arxiv.org/abs/2402.00705).

ℹ️ Check out ([important dates](https://preferdatachallenge.nl/#important-dates)) to see when this challenge phase will open and close.

## Prerequisites

1. Make a copy of [this](https://github.com/eyra/fertility-prediction-challenge) template repository, by forking and cloning as explained [here](https://github.com/eyra/fertility-prediction-challenge/wiki#how-to-fork-and-clone-this-repository).
2. Make sure to allow Github Actions on your own repository: Go to the “Actions” tab and click “I understand my workflows, go ahead and enable them.”
3. If you have not already done so, download the training data and codebooks via the "Download data" task on the Next platform. **Important**: you are not allowed to share these datasets and you **may not** upload them to your Github repository!

ℹ️ Click [here](https://preferdatachallenge.nl/posts/posts/2024-03-20-prefer-datasets.html) for a detailed explanation on the datasets that you have downloaded. Click [here](https://preferdatachallenge.nl/posts/posts/2024-03-21-prefer-codebooks.html) for an explanation on how to use the codebooks. 

## Prepare your method

To participate in the challenge you need to submit a method (i.e. code for data preprocessing, training, and making predictions, and the trained model) using this repository. 

ℹ️ You can use either Python or R for your method. By default, Python is used. For Python this repo assumes that your method uses the [Anaconda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html) Python distribution.

1. **Choose your programming language**: the default set-up is Python, if you would like to use R, go to ```settings.json``` and change ```{"dockerfile": "python.Dockerfile"}``` into ```{"dockerfile": "r.Dockerfile"}```. Read [here](https://github.com/eyra/fertility-prediction-challenge/wiki#how-to-update-files-in-your-forked-repository) how to update files in your forked repository. 

2. **Choose the main script to work with**: go to ```submission.py``` (Python) or ```submission.R``` (R) depending on your preferred programming language. 

3. **Preprocess the data**: any steps to clean or preprocess the data need to be documented within the function ```clean_df``` in the `submission.py` / `submission.R` script (depending on your preferred programming language). *Note*: The function ```clean_df``` will also be applied to the holdout data when you submit your model. At this point, the [codebooks](https://preferdatachallenge.nl/posts/posts/2024-03-21-prefer-codebooks.html) can be useful to make sense of the data.

4. **Train, tune, and save your model**: any steps to train your model need to be documented (e.g., code for the model, number of folds, set seed) within the  `training.py` / `training.R` script. The only function in this script is `train_save_model` in which you can put the steps needed to run the model. The output of this script is your saved model, either ```model.joblib``` or  ```model.rds```. Make sure that your model is saved in the same folder as `submission.py`/`submission.R` under the name `model.joblib` (for Python) or `model.rds` (for R). The model will be applied to the holdout data when you submit your model. 

5. **Test your model on fake data**: you can test your ```clean_df``` function and your model (stored in:  ```model.joblib```/```model.rds```) on fake data (`PreFer_fake_data.csv`) through the function ```predict_outcomes```. You will also need to adapt this function such that the outputs of your model are predicted classes (i.e., 0s and 1s) rather than, for example, probabilities. If you passed the test (i.e.```predict_outcomes``` led to predictions rather than errors), you can submit your method. If your method does not run on the "fake data", it will not run on the holdout data. [If you "push" your method to Github this test will also be automatically run.] 

6. ***Submit your method***: Submit your method as explained [here](https://github.com/eyra/fertility-prediction-challenge/tree/master#submit-your-method).
  
[Here](https://preferdatachallenge/posts) are a bunch of videos and guides, notebooks, and blogs available that guide you through this process. 

### (Adding) libraries / packages
For **Python** users: please see the ```environment.yml``` file to see which libraries are installed per default. You can add or remove libraries from this ```environment.yml``` file as you desire. It is recommended to state particular versions (i.e., `pandas=1.5` rather than `pandas>=1.5`). You have to call upon those libraries in the `submission.py` file.

For **R** users: no packages are pre-installed. You can use the ```packages.R``` file and add the names of the packages to the code: ```install.packages(c("dplyr","data.table","tidyr"), repos="https://cran.r-project.org")```. You have to call upon those libraries in the `submission.R` file. (i.e., adding ```library(c("dplyr","data.table","tidyr"))```)


### Submit your method

Follow the instructions below to submit your method:

1. Make sure that you describe your model in the `description.md` file in your GitHub repository and commit changes (i.e. save changes locally)
2. Push the commit (i.e. upload changed version to your online repository). **Important**: make sure that you only push the relevant files and make sure that you **do not upload any of the datasets**. 
3. In GitHub make sure that the checks pass:

![](https://github.com/eyra/fertility-prediction-challenge/blob/master/images/Checks%20passed.png)

ℹ️ If the check fails go to [FAQ](https://github.com/eyra/fertility-prediction-challenge/wiki#frequently-asked-questions). You might need to add dependencies as described [here](https://github.com/eyra/fertility-prediction-challenge/wiki#how-to-add-dependencies). You can also test your implementation locally as explained [here](https://github.com/eyra/fertility-prediction-challenge/wiki#how-to-test-your-implementation).

4. On the main page of your repository, above the file list, click commits to view a list of commits, as described [here](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits#about-commit-branches-and-tag-labels)
5. Go to the commit that you want to submit and right click on view commit details, then click "Copy Link Address", see example below:

![](https://github.com/eyra/fertility-prediction-challenge/blob/master/images/Copy%20link%20to%20commit.png)

6. Add a submission on the Next platform by providing the URL to your GitHub commit (copied at step 5), this commit will serve as your submission to the challenge.

## Leaderboards

The [LISS panel](https://www.centerdata.nl/en/liss-panel) challenge data is separated into an example dataset for tuning your method and a holdout dataset that will be used to validate your method performance. After [submission](https://github.com/eyra/fertility-prediction-challenge/tree/master#how-to-submit-your-method) your method will be run on the holdout data. Your performance scores on the holdout data will be added to the leaderboards, so your scores can be compared to the performance scores of other methods.

ℹ️ Leaderboards are generated at fixed time points, check out ([important dates](https://preferdatachallenge.nl/#important-dates)) for leaderboard submission deadlines. 


The following leaderboards will be available:

- [F1](https://www.educative.io/answers/what-is-the-f1-score)\*
- [Precision](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall)\*
- [Recall](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall)\*
- Overall [accuracy](https://developers.google.com/machine-learning/crash-course/classification/accuracy)

\*_For the prediction of having a child in 2021-2023 (positive class)_.

For this challenge the F1 leaderboard is the main leaderboard.

ℹ️ The Python code to calculate the metric scores used to create the challenge leaderboards is included in this repo. Check out [score.py](https://github.com/eyra/fertility-prediction-challenge/blob/master/score.py).

## PreFer Challenge scope

### Research problem
Accurate predictions of the number and timing of children are crucial for effective resource allocation in society. However, despite many studies in the social sciences, we have no clear understanding of which factors are most important for fertility prediction or how well we are able to predict fertility behaviour.

### Purpose statement
To gain insight into how well methods are able to predict fertility within a three year period (2021-2023), based on survey data from previous years (2007-2020) of people in the [LISS panel](https://www.centerdata.nl/en/liss-panel) who were aged 18-45 in 2020. The LISS panel is a representative online longitudinal panel of Dutch households.

## License

This project is licensed under the terms of the [MIT license](https://github.com/eyra/fertility-prediction-challenge/blob/master/LICENSE).

## Acknowledgements

The code in this repository is developed by [Eyra](https://eyra.co/) as part of the Rank program funded by [ODISSEI](https://odissei-data.nl/en/) and the [NWO VIDI grant](https://www.rug.nl/gmw/news/210714-vidi-gert-stulp?lang=en) awarded to Gert Stulp. The [LISS panel](https://www.centerdata.nl/en/liss-panel) data is provided by [Centerdata](https://www.centerdata.nl/).
