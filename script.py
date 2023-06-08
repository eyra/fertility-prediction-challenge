"""
This script is used to generate the outcome variable for the data set.

The script should be modified to implement your own logic for generating 
the outcome variable. 

When chaning the script focus on the process function. The process function
takes a CSV reader and CSV writer object. 

The reader object is used to read the input. Iterating over it yields a 
dictionary for each row. The writer object is used to write the output. 

The writer object is a DictWriter object. It is already configured with the
correct columns. Use the writerow method to create the expected results using
as dictionary with the nomem_encr and outcome keys.

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

    # Change the following code to implement your own logic. The current implementation 
    # uses the year variable to generate the outcome variable. The outcome variable 
    # is 1 if the year is odd and 0 if the year is even.
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
