# Fertility Benchmark Submission

This repository is a template that can be used to submit your Python method for the Fertility prediction benchmark challenge. To participate in the challenge walk through the following steps:

1. Register and sign in on this website [link will be added] using your institution email address.
2. Download the participant data to tune and test your method.
3. Fork this repository as explained in the [getting started](https://github.com/eyra/eyra-rank-template/edit/main/README.md#getting-started) section.
4. Change the algorithm.py file to include your method. Make sure that the expected input and output data format does not change.
5. Add dependencies when required as explained [here](https://github.com/eyra/eyra-rank-template/edit/main/README.md#dependencies).
6. Test your implementation as explained [here](https://github.com/eyra/eyra-rank-template/edit/main/README.md#testing).
7. Submit your method as explained [here](https://github.com/eyra/eyra-rank-template/edit/main/README.md#submitting-your-method).

After submission, your method will be run on the holdout dataset and the outcomes of your method will be compared to the ground truth in the holdout dataset with respect to:

- [accuracy](https://developers.google.com/machine-learning/crash-course/classification/accuracy)
- [precision](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall), [recall](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall) and [F1](https://www.educative.io/answers/what-is-the-f1-score) for the positive class (having a child in the 2020-2022).

## Getting Started

To get started, fork the GitHub repository, follow these steps:

1. Go to the repository's GitHub page (likely this page)
2. Click on the "Fork" button in the top right corner of the page.
3. Select the account or organization where you want to fork the repository.
4. Wait for the forking process to complete.
5. Once the forking process is complete, you will have a copy of the repository
   in your own GitHub account or organization.

After forking the repository, clone it to your local machine:

```bash
git clone https://github.com/<your-username>/python-algorithm-template.git
```

Then, modify the algorithm.py file to implement your own algorithm.

## Dependencies

Dependencies need to be added to the `environment.yml`. They can be copied from
the output of the following command:

```bash
conda env export
```

## Testing

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

## Scoring

To score your predictions you can use the script in scoring mode. Run the score
part of the script using the following command:

```bash
python3 script.py score predictions.csv data/test_data_liss_2_subjects_ground_truth.csv
```

Replace `predictions.csv` and `data/test_data_liss_2_subjects_ground_truth.csv`
with the actual paths to your prediction and ground truth files.

After running the command, the output will show the accuracy, precision, recall,
and F1 score of the predictions.

## Submitting your method

Follow the instructions below to submit your method:

1. Ensure that the script works by running the [Docker command](https://github.com/eyra/eyra-rank-template/edit/main/README.md#docker).
2. Commit changes (i.e. save changes locally)
3. Push the commit (i.e. upload changed version to your online repository)
4. Sign in on this website [link will be added]
5. Provide the URL to your repository on GitHub.
6. When you click "Submit", your latest commit in this repository will serve as your submission to the benchmark challenge.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

# eyra-fertility-prediction-challenge
