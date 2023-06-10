# Fertility Prediction Benchmark Submission
This is a template repository to submit your Python method for the Fertility Prediction Benchmark Challenge, organized by [Lisa Sivak](https://www.rug.nl/staff/e.sivak/cv) and [Gert Stulp](https://www.rug.nl/staff/g.stulp/). 

After submission, your method will be run on the holdout dataset and the outcomes of your method will be compared to the ground truth outcomes in the holdout dataset with respect to: 
- [accuracy](https://developers.google.com/machine-learning/crash-course/classification/accuracy)
- [precision](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall), [recall](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall) and [F1](https://www.educative.io/answers/what-is-the-f1-score) for the positive class (having a child in the 2020-2022). 

To participate in the challenge follow these steps:

1. Register and sign in on this website [link will be added] using your institution email address.
2. Download the example data to tune and test your method: 
   - The LISS_example_input_data can be used as input for your method
   - The LISS_example_groundtruth_data can be used to validate your predictions
   Feel free to 
3. Fork this repository as explained in the [getting started](https://github.com/eyra/eyra-rank-template/edit/main/README.md#getting-started) section. 
4. Change the process function of the [script.py](https://github.com/eyra/eyra-fertility-prediction-challenge/blob/master/script.py) file to include your method. Make sure that the expected input and output data format does not change.
5. Add dependencies when required as explained [here](https://github.com/eyra/eyra-rank-template/edit/main/README.md#dependencies).
6. Test your implementation as explained [here](https://github.com/eyra/eyra-rank-template/edit/main/README.md#testing). 
7. Submit your method as explained [here](https://github.com/eyra/eyra-rank-template/edit/main/README.md#submitting-your-method).

ℹ️ This repo assumes that your method uses the [miniconda3](https://docs.conda.io/en/latest/miniconda.html) Python distribution. 

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
docker run -v "$(pwd)/data:/data" eyra-rank /data/test_data_liss_2_subjects.csv
```

### Miniconda

To test your implementation directly via miniconda, first create a new conda environment:

```bash
conda env create -f environment.yml --no-default-packages
conda activate eyra-rank
```

Then, run script.py:

```bash
python script.py
```

## Submitting your method

Follow the instructions below to submit your method:

1. Ensure that the script works by running the [Docker command](https://github.com/eyra/eyra-rank-template/edit/main/README.md#docker).
2. Commit changes (i.e. save changes locally)
3. Push the commit (i.e. upload changed version to your online repository)
4. Sign in on this website [link will be added]
5. Provide the URL to your repository on GitHub.
6. When you click "Submit", your latest commit in this repository will serve as your submission to the benchmark challenge.

## License

This project is licensed under the terms of the MIT license - see the LICENSE file for details.

## Acknowledgements

The code in this repository is developed by [Eyra](https://eyra.co/) as part of the benchmark infrastructure starter kit project funded by [ODISSEI](https://odissei-data.nl/en/) and the [NWO VIDI grant](https://www.rug.nl/gmw/news/210714-vidi-gert-stulp?lang=en) awarded to Gert Stulp. The [LISS panel](https://www.centerdata.nl/en/liss-panel) data is provided by [Centerdata](https://www.centerdata.nl/).    

