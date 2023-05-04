from pyspark import SparkContext
import sys
import csv

sys.path.append("./")
from utilities.requests import find_user_agent

input_dir = ""
output_filename = ""

if __name__ == "__main__":
    try:
        input_dir = sys.argv[1]
    except IndexError:
        raise Exception("Please provide the input file(s) directory.")

    try:
        output_filename = sys.argv[2]
    except IndexError:
        raise Exception("Please provide the output file location / name.")

sc = SparkContext(appName="Collect User Agents")

textFiles = sc.wholeTextFiles(path=input_dir)

all_user_agents_rdd = textFiles.map(find_user_agent)

distinct_user_agents_rdd = all_user_agents_rdd.distinct()

distinct_user_agents_list = distinct_user_agents_rdd.collect()

sc.stop()

out_file = open(output_filename, 'w+', newline='')
csv_writer = csv.writer(out_file)
csv_writer.writerow(distinct_user_agents_list)

print(distinct_user_agents_list)
