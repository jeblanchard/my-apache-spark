from pyspark import SparkContext

import sys

sys.path.append("./")
from utilities.requests import find_user_agent

file_path = ""
if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
    except IndexError:
        raise Exception("Please provide the input file(s) location.")

sc = SparkContext("local", "test")

textFiles = sc.wholeTextFiles(path=file_path)

all_user_agents_rdd = textFiles.map(find_user_agent)

distinct_user_agents_rdd = all_user_agents_rdd.distinct()

distinct_user_agents_list = distinct_user_agents_rdd.collect()

print(distinct_user_agents_list)
