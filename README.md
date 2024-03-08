# Fertility Prediction Challenge (PreFer)

This is a template repository to submit your method for phase 1 of the Fertility Prediction Challenge ([PreFer](https://preferdatachallenge.nl)). You can read [here](https://preferdatachallenge.nl/#how-to-participate) how to participate in the challenge.

## Benchmark

Accurate predictions of the number and timing of children are crucial for effective resource allocation in society. However, despite many studies in the social sciences, we have no clear understanding of which factors are most important for fertility prediction or how well we are able to predict fertility behaviour.

This benchmark aims to gain insight into how well methods are able to predict fertility within a three year period (2021-2023), based on survey data from previous years (2007-2020) of people in the [LISS Panel](https://www.centerdata.nl/en/liss-panel) who were aged 18-45 in 2020. The LISS Panel is a representative online longitudinal panel of Dutch households.

## Challenge (Phase 1)

The challenge is to predict whether an individual will have a child within a three year period (2021-2023), based on survey data from previous years (2007-2020). Data about family and children, partnerships, education, income, employment, health, and more can be used for prediction.

Check out ([important dates](https://preferdatachallenge.nl/#important-dates)) to see when this challenge phase will open and close.

During this challenge phase, the Liss dataset is used, which is split into a training and holdout dataset as described [here](https://stulp.gmw.rug.nl/prefer/details/overview/2data.html#liss-dataset). You can use the training dataset to tune your method. When you have prepared your method, you can submit it through the Next platform, after which it will be run and evaluated on the holdout dataset and your result will be added to the challenge leaderboard.

### Preparation

1. If you have [registered](https://preferdatachallenge.nl/details/overview/3application.html) for the PreFer challenge, you will receive a link for participation.
2. Visit the Next platform and sign in to download the training data.
3. Fork and clone [this](https://github.com/eyra/fertility-prediction-challenge) repository as explained [here](https://github.com/eyra/fertility-prediction-challenge/wiki#how-to-fork-and-clone-this-repository).

ℹ️ You can use either Python or R for your method. For Python this repo assumes that your method uses the [Anaconda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html) Python distribution.

### Participation [Work in progress]

1. After you have forked and cloned this repository (see preparation), you can start adding your method.
2. Go to submission.py or submission.R depending on your preferred programming language. These files contain example scripts.
3. Develop your prediction method (i.e. train your model). To participate in the challenge you need to adjust the submission script to include your method. This is the script that will be run on the holdout data after submission.
4. Add data cleaning (preprocessing) to clean_df(df) 

Change the content of the **predict_outcomes function** in [submission.py](https://github.com/eyra/fertility-prediction-challenge/blob/master/src/submission.py) as explained in the script to include your method. Do not change the expected input and output data format.
6. The metrics used to create the challenge [leaderboards](https://github.com/eyra/fertility-prediction-challenge/tree/master#leaderboard) are included in this repo. You can separate the challenge example data into a train and test set and use the score function in [submission.py](https://github.com/eyra/fertility-prediction-challenge/blob/master/src/submission.py) to determine your method performance scores on the example data as described [here](https://github.com/eyra/fertility-prediction-challenge/wiki#how-to-evaluate-your-method).
7. Submit your method as explained [here](https://github.com/eyra/fertility-prediction-challenge/tree/master#how-to-submit-your-method).
8. Your performance scores on the challenge [leaderboards](https://github.com/eyra/fertility-prediction-challenge/tree/master#leaderboard) will become available after signing in on the Next platform ([Round 1](https://eyra.co/benchmark/5), [Round 2](https://eyra.co/benchmark/6)).

ℹ️ It takes some time to process the results for the leaderboards.

### Leaderboards

The [LISS Panel](https://www.centerdata.nl/en/liss-panel) challenge data is separated into an example dataset for tuning your method and a holdout dataset that will be used to validate your method performance. After [submission](https://github.com/eyra/fertility-prediction-challenge/tree/master#how-to-submit-your-method) your method will be run on the holdout data. Your performance scores on the holdout data will be added to the leaderboards, so your scores can be compared to the performance scores of other methods.

The following leaderboards will be available:

- [F1](https://www.educative.io/answers/what-is-the-f1-score)\*
- [Precision](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall)\*
- [Recall](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall)\*
- Overall [accuracy](https://developers.google.com/machine-learning/crash-course/classification/accuracy)

\*_For the prediction of having a child in 2020-2022 (positive class)_.

For this challenge the F1 leaderboard is the main leaderboard.

## How to submit your method?

Follow the instructions below to submit your method:

1. Make sure that you describe your model in the readme.md file in your GitHub repository and commit changes (i.e. save changes locally)
2. Push the commit (i.e. upload changed version to your online repository)
3. In GitHub make sure that the checks pass:

![](https://github.com/eyra/fertility-prediction-challenge/blob/master/images/Checks%20passed.png)

ℹ️ If the check fails go to [FAQ](https://github.com/eyra/fertility-prediction-challenge/wiki#frequently-asked-questions), you might need to add dependencies as described [here](https://github.com/eyra/fertility-prediction-challenge/wiki#how-to-add-dependencies), you can also test your implementation as explained [here](https://github.com/eyra/fertility-prediction-challenge/wiki#how-to-test-your-implementation).

4. On the main page of your repository, above the file list, click commits to view a list of commits, as described [here](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits#about-commit-branches-and-tag-labels)
5. Go to the commit that you want to submit and right click on view commit details, then click "Copy Link Address", see example below:

![](https://github.com/eyra/fertility-prediction-challenge/blob/master/images/Copy%20link%20to%20commit.png)

6. Add a submission on the Next platform ([Round 1](https://eyra.co/benchmark/5), [Round 2](https://eyra.co/benchmark/6)) by providing the URL to your GitHub commit (copied at step 5), this commit will serve as your submission to the challenge.

## License

This project is licensed under the terms of the [MIT license](https://github.com/eyra/fertility-prediction-challenge/blob/master/LICENSE).

## Acknowledgements

The code in this repository is developed by [Eyra](https://eyra.co/) as part of the benchmark infrastructure starter kit project funded by [ODISSEI](https://odissei-data.nl/en/) and the [NWO VIDI grant](https://www.rug.nl/gmw/news/210714-vidi-gert-stulp?lang=en) awarded to Gert Stulp. The [LISS panel](https://www.centerdata.nl/en/liss-panel) data is provided by [Centerdata](https://www.centerdata.nl/).
