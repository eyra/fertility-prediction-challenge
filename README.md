# Fertility Prediction Benchmark Challenge Submission
This is a template repository to submit your Python method for the Fertility Prediction Benchmark Challenge, organized by [Lisa Sivak](https://www.rug.nl/staff/e.sivak/cv) and [Gert Stulp](https://www.rug.nl/staff/g.stulp/). You can read [here](https://github.com/eyra/fertility-prediction-challenge/tree/master#participation) how to participate in the challenge. 

## Benchmark
Accurate predictions of the number and timing of children are crucial for effective resource allocation in society. However, despite many studies in the social sciences, we have no clear understanding of which factors are most important for fertility prediction or how well we are able to predict fertility behaviour. 

This benchmark aims to gain insight into how well methods are able to predict fertility within a three year period (2020-2022), based on survey data from previous years (2007-2019) of people in the [LISS Panel](https://www.centerdata.nl/en/liss-panel) who were aged 18-45 in 2019. The LISS Panel is a representative online longitudinal panel of Dutch households.

## Challenge
The challenge is to predict whether an individual will have a child within a three year period (2020-2022), based on survey data from previous years (2007-2019). Data about family and children, partnerships, education, income, employment, health, and more can be used for prediction.

### Participation
To participate in the challenge follow these steps:

1. Make sure you have filled out the [LISS panel Data Statement](https://statements.centerdata.nl/liss-panel-data-statement) form. 
2. Register and sign in on this website [link will be added] using your institution email address.
3. Download the example data to tune and test your method: 
   - LISS_example_input_data.csv: data that can be used for predictions
   - LISS_example_groundtruth_data.csv: contains outcome per individual (0=no child, 1=child) for training and testing
4. Fork and clone the fertility-prediction-challenge repository as explained [here](https://github.com/eyra/fertility-prediction-challenge/tree/master#how-to-fork-and-clone-this-repository). 
5. Add dependencies when required as explained [here](https://github.com/eyra/fertility-prediction-challenge/tree/master#how-to-add-dependencies).
6. Change the content of the predict_outcomes function in [script.py](https://github.com/eyra/fertility-prediction-challenge/blob/master/src/script.py) as explained in the script to include your method. Do not change the expected input and output data format.
7. The metrics used to create the challenge [leaderboards](https://github.com/eyra/fertility-prediction-challenge/tree/master#leaderboard) are included in this repo. You can separate the challenge example data into a train and test set and use the score function in [script.py](https://github.com/eyra/fertility-prediction-challenge/blob/master/src/script.py) to evaluate the performance of your method on the example data as described [here](https://github.com/eyra/fertility-prediction-challenge/tree/master#how-to-evaluate-your-method). 
8. To make sure your challenge submission will work (your method will run on the holdout data), test your implementation as explained [here](https://github.com/eyra/fertility-prediction-challenge/tree/master#how-to-test-your-implementation). 
9. Submit your method as explained [here](https://github.com/eyra/fertility-prediction-challenge/tree/master#how-to-submit-your-method).
10. Your results on the holdout data and your rank on the leaderboards will become available after signing in on this website [link will be added]. ❗️NB: It takes some time to process the results.

ℹ️ This repo assumes that your method uses the [miniconda3](https://docs.conda.io/en/latest/miniconda.html) Python distribution. 

### Leaderboards
The [LISS Panel](https://www.centerdata.nl/en/liss-panel) challenge data is separated into an example dataset for tuning your method and a holdout dataset that will be used to validate your method performance. After [submission](https://github.com/eyra/fertility-prediction-challenge/tree/master#how-to-submit-your-method) your method will be run on the holdout data. Your evaluation scores on the holdout data will be added to the leaderboards, so your scores can be compared to the performance scores of other methods.

The following leaderboards will be available: 
- [F1](https://www.educative.io/answers/what-is-the-f1-score)* 
- [Precision](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall)*
- [Recall](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall)* 
- Overall [accuracy](https://developers.google.com/machine-learning/crash-course/classification/accuracy)

*_For the prediction of having a child in 2020-2022 (positive class)_.

For this challenge the F1 leaderboard is the main leaderboard. 

## How to fork and clone this repository?

To fork and clone [this repository](https://github.com/eyra/fertility-prediction-challenge), follow these steps:

1. On the [GitHub page](https://github.com/eyra/fertility-prediction-challenge) click the "Fork" button in the top right corner of the page.
2. Select the account or organization where you want to fork the repository.
3. Wait for the forking process to complete.
4. Once the forking process is complete, you will have a copy of the repository
   in your own GitHub account or organization.
5. After forking the repository, clone it to your local machine:

```bash
git clone https://github.com/<your-username>/fertility-prediction-challenge.git
```

## How to add dependencies?

Dependencies need to be added to the `environment.yml`. They can be copied from
the output of the following command:

```bash
conda env export
```

## How to evaluate your method?

To score your predictions you can use the script in scoring mode. Run the score
part of the script using the following command:

```bash
python3 script.py score predictions.csv data/test_data_liss_2_subjects_ground_truth.csv
```

Replace `predictions.csv` and `data/test_data_liss_2_subjects_ground_truth.csv`
with the actual paths to your prediction and ground truth files.

After running the command, the output will show the accuracy, precision, recall,
and F1 score of the predictions.

## How to test your implementation?

You can test your implementation either via Docker or directly via miniconda.

### Docker

First, install Docker from [their website](https://www.docker.com).
To test your implementation via Docker, build the Docker image:

```bash
docker build -t eyra-rank .
```

Then, run the Docker container:

```bash
docker run eyra-rank
```

This should run the script with the example data. You can run it against other data
using:

```bash
docker run -v "$(pwd)/data:/data"  eyra-rank predict /data/test_data_liss_2_subjects.csv
```

### Miniconda

To test your implementation directly via miniconda, first create a new conda environment:

```bash
conda env create -f environment.yml --no-default-packages
conda activate eyra-rank
```

Then, run the script:

```bash
python3 script.py predict
```

## How to submit your method?

Follow the instructions below to submit your method:

1. Ensure that the script works by running the [Docker command](https://github.com/eyra/fertility-prediction-challenge/tree/master#docker).
2. Commit changes (i.e. save changes locally)
3. Push the commit (i.e. upload changed version to your online repository)
4. Sign in on this website [link will be added]
5. Provide the URL to your repository on GitHub.
6. When you click "Submit", your latest commit in this repository will serve as your submission to the benchmark challenge.

## License
This project is licensed under the terms of the [MIT license](https://github.com/eyra/fertility-prediction-challenge/blob/master/LICENSE).

## Acknowledgements

The code in this repository is developed by [Eyra](https://eyra.co/) as part of the benchmark infrastructure starter kit project funded by [ODISSEI](https://odissei-data.nl/en/) and the [NWO VIDI grant](https://www.rug.nl/gmw/news/210714-vidi-gert-stulp?lang=en) awarded to Gert Stulp. The [LISS panel](https://www.centerdata.nl/en/liss-panel) data is provided by [Centerdata](https://www.centerdata.nl/).    
