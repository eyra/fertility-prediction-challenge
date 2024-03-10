# Fertility Prediction Challenge (PreFer)

This is a template repository to submit your method for phase 1 of the Fertility Prediction Challenge ([PreFer](https://preferdatachallenge.nl)). You can read [here](https://preferdatachallenge.nl/#how-to-participate) how to participate in the challenge.

## Research problem
Accurate predictions of the number and timing of children are crucial for effective resource allocation in society. However, despite many studies in the social sciences, we have no clear understanding of which factors are most important for fertility prediction or how well we are able to predict fertility behaviour.

## Purpose statement
To gain insight into how well methods are able to predict fertility within a three year period (2021-2023), based on survey data from previous years (2007-2020) of people in the [LISS Panel](https://www.centerdata.nl/en/liss-panel) who were aged 18-45 in 2020. The LISS Panel is a representative online longitudinal panel of Dutch households.

## Challenge

The challenge is to predict whether an individual will have a child within a three year period (2021-2023), based on survey data from previous years (2007-2020). Data about family and children, partnerships, education, income, employment, health, and more can be used for prediction.

During this challenge phase, the Liss dataset is used, which is split into a training and holdout dataset as described [here](https://stulp.gmw.rug.nl/prefer/details/overview/2data.html#liss-dataset). You can use the training dataset to tune your method. When you have prepared your method, you can submit it through the Next platform, after which it will be run and evaluated on the holdout dataset and your result will be added to the challenge leaderboard.

ℹ️ Check out ([important dates](https://preferdatachallenge.nl/#important-dates)) to see when this challenge phase will open and close.

### Prerequisites

1. If you have [registered](https://preferdatachallenge.nl/details/overview/3application.html) for the PreFer challenge, you will receive a link for participation.
2. Visit the Next platform and sign in to download the training data. This data consists of:
    1. ```PreFer_training_data.csv``` (training dataset that can be used for predicting outcomes)
    2. ```PreFer_training_outcome.csv``` (ground truth outcome for the training dataset)
    3. ```PreFer_training_background_data.csv``` (optional additional dataset with more detailed values (monthly) for a limited number of demographic and socio-economic variables)
    4. ```PreFer_training_supplementary_data.csv``` (optional additional dataset with data from LISS respondents that are not included in the challenge data sample of 18-45 year olds in 2020)

### Prepare your method
To participate in the challenge you need to submit a method using this repository. 

ℹ️ You can use either Python or R for your method. By default, Python is used. For Python this repo assumes that your method uses the [Anaconda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html) Python distribution.

Follow the steps below to prepare your method for submission:

1. Make a copy of [this](https://github.com/eyra/fertility-prediction-challenge) template repository, by forking and cloning as explained [here](https://github.com/eyra/fertility-prediction-challenge/wiki#how-to-fork-and-clone-this-repository).
2. If you are using R, go to ```settings.json``` and change ```{"dockerfile": "python.Dockerfile"}``` into ```{"dockerfile": "r.Dockerfile"}```.
3. Go to submission.py (Python) or submission.R (R) depending on your preferred programming language. 
4. Adjust ```clean_df``` to clean (preprocess) the data according to your preferences.
5. Adjust ```predict_outcomes``` to add your prediction method.
6. Test your method on the “fake” data in the [data folder](https://github.com/eyra/fertility-prediction-challenge/tree/master/data) **[coming soon]**. If you encounter errors, debug your method until it works. If your method does not run on the “fake” data, it will not run on the holdout data either and your submission will not result in a place on the challenge leaderboard.
7. Submit your method as explained [here](https://github.com/eyra/fertility-prediction-challenge/tree/master#submit-your-method).
   
ℹ️ Leaderboards are generated at fixed time points, check out ([important dates](https://preferdatachallenge.nl/#important-dates)) for leaderboard submission deadlines.

### Submit your method

Follow the instructions below to submit your method:

1. Make sure that you describe your model in the readme.md file in your GitHub repository and commit changes (i.e. save changes locally)
2. Push the commit (i.e. upload changed version to your online repository)
3. In GitHub make sure that the checks pass **[currently the checks do not pass, this will be fixed once the fake data is added to the repo]**:

![](https://github.com/eyra/fertility-prediction-challenge/blob/master/images/Checks%20passed.png)

ℹ️ If the check fails go to [FAQ](https://github.com/eyra/fertility-prediction-challenge/wiki#frequently-asked-questions), you might need to add dependencies as described [here](https://github.com/eyra/fertility-prediction-challenge/wiki#how-to-add-dependencies), you can also test your implementation as explained [here](https://github.com/eyra/fertility-prediction-challenge/wiki#how-to-test-your-implementation).

4. On the main page of your repository, above the file list, click commits to view a list of commits, as described [here](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits#about-commit-branches-and-tag-labels)
5. Go to the commit that you want to submit and right click on view commit details, then click "Copy Link Address", see example below:

![](https://github.com/eyra/fertility-prediction-challenge/blob/master/images/Copy%20link%20to%20commit.png)

6. Add a submission on the Next platform by providing the URL to your GitHub commit (copied at step 5), this commit will serve as your submission to the challenge.

## Leaderboards

The [LISS Panel](https://www.centerdata.nl/en/liss-panel) challenge data is separated into an example dataset for tuning your method and a holdout dataset that will be used to validate your method performance. After [submission](https://github.com/eyra/fertility-prediction-challenge/tree/master#how-to-submit-your-method) your method will be run on the holdout data. Your performance scores on the holdout data will be added to the leaderboards, so your scores can be compared to the performance scores of other methods.

The following leaderboards will be available:

- [F1](https://www.educative.io/answers/what-is-the-f1-score)\*
- [Precision](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall)\*
- [Recall](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall)\*
- Overall [accuracy](https://developers.google.com/machine-learning/crash-course/classification/accuracy)

\*_For the prediction of having a child in 2020-2022 (positive class)_.

For this challenge the F1 leaderboard is the main leaderboard.

Change the content of the **predict_outcomes function** in [submission.py](https://github.com/eyra/fertility-prediction-challenge/blob/master/src/submission.py) as explained in the script to include your method. Do not change the expected input and output data format.
6. The metrics used to create the challenge [leaderboards](https://github.com/eyra/fertility-prediction-challenge/tree/master#leaderboard) are included in this repo. You can separate the challenge example data into a train and test set and use the ```score(prediction_path, ground_truth_path, output)``` function in [run.py](https://github.com/eyra/fertility-prediction-challenge/blob/master/run.py) to determine your method performance scores on the example data as described [here](https://github.com/eyra/fertility-prediction-challenge/wiki#how-to-evaluate-your-method).
7. Submit your method as explained [here](https://github.com/eyra/fertility-prediction-challenge/tree/master#how-to-submit-your-method).
8. Your performance scores on the challenge [leaderboards](https://github.com/eyra/fertility-prediction-challenge/tree/master#leaderboard) will become available after signing in on the Next platform ([Round 1](https://eyra.co/benchmark/5), [Round 2](https://eyra.co/benchmark/6)).

## License

This project is licensed under the terms of the [MIT license](https://github.com/eyra/fertility-prediction-challenge/blob/master/LICENSE).

## Acknowledgements

The code in this repository is developed by [Eyra](https://eyra.co/) as part of the benchmark infrastructure starter kit project funded by [ODISSEI](https://odissei-data.nl/en/) and the [NWO VIDI grant](https://www.rug.nl/gmw/news/210714-vidi-gert-stulp?lang=en) awarded to Gert Stulp. The [LISS panel](https://www.centerdata.nl/en/liss-panel) data is provided by [Centerdata](https://www.centerdata.nl/).
