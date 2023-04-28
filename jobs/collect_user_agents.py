from pyspark import SparkContext
from utilities.requests import find_user_agent

sc = SparkContext("local", "test")

textFiles = sc.wholeTextFiles(path="./work-dir/")

all_user_agents_rdd = textFiles.map(find_user_agent)

distinct_user_agents_rdd = all_user_agents_rdd.distinct()

distinct_user_agents_list = distinct_user_agents_rdd.collect()

print(distinct_user_agents_list)
