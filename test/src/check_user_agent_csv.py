import csv
import sys

try:
    job_output_filename = sys.argv[1]
except IndexError:
    raise Exception("Please provide the job output filename.")

out_file = open(job_output_filename, 'r', newline='')
csv_reader = csv.reader(out_file)

expected_list = ["GoogleHC/1.0"]

actual_list = []
for row in csv_reader:
    for item in row:
        actual_list.append(item)

if expected_list == actual_list:
    print("Test passed. User agent list is correct.")
else:
    raise Exception(f"Test failed. User agent list is wrong.\n"
                    f"Actual: {actual_list}\n"
                    f"Expected: {expected_list}\n"
                    )
