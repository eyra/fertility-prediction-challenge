"""
This is an example script to generate the outcome variable for the dataset.

This script should be modified to prepare your own submission that predicts 
the outcome for the benchmark challenge by changing the process function. 

The process function takes a CSV reader and CSV writer object. The reader object 
is used to read the input. Iterating over it yields a dictionary for each row. 
The writer object is used to write the output. 

The writer object is a DictWriter object, which is pre-configured with the
correct columns. Use the writerow method to write the expected results using
a dictionary with the nomem_encr and outcome keys.

The script can be run from the command line using the following command:

python script.py input_path 

An example for the provided test is:

python script.py data/test_data_liss_2_subjects.csv
"""

import csv
import sys
import argparse


parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument(
    "input_path", metavar="input_path", type=str, help="path to input CSV file"
)
parser.add_argument(
    "--output_path", metavar="output_path", type=str, help="path to output CSV file"
)


def process(reader, writer):
    """Process the input CSV file and write the output CSV file."""

    # Add your method here.  

    # Use the code below to write the outcome you predict per nomem_encr.
    # The implementation below is a dummy method predicting 1 if the year is odd
    # and 0 if the year is even. Replace this with the outcome from your method.
    for row in reader:
        writer.writerow(
            {"nomem_encr": row["nomem_encr"], "outcome": int(int(row["year"]) % 2)}
        )


def main(input_path, output_path):
    if output_path is None:
        output = sys.stdout
    else:
        output = open(output_path, "w")
    writer = csv.DictWriter(output, fieldnames=["nomem_encr", "outcome"])
    writer.writeheader()
    try:
        with open(input_path) as f:
            reader = csv.DictReader(f)
            process(reader, writer)
    finally:
        output.close()


if __name__ == "__main__":
    args = parser.parse_args()
    main(args.input_path, args.output_path)
