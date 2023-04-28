from pyspark import SparkContext
import re

user_agent_pattern = re.compile(r"\'User-Agent\',\s(\w*)", re.IGNORECASE)

print("loaded the file correctly")


def find_user_agent(filename_content_tuple):
    request_str = filename_content_tuple[1]

    user_agent_match = user_agent_pattern.search(request_str)

    if not user_agent_match:
        return ""

    user_agent = user_agent_match.group(1)
    return user_agent


sc = SparkContext("local", "test")
textFiles = sc.wholeTextFiles(path="test/data/")

allUserAgents = textFiles.map(find_user_agent)
print("Got to all user agents")

distinctUserAgents = allUserAgents.distinct()
print("Got to distinct user agents")
print(distinctUserAgents)

distinctUserAgents.collect()

print(distinctUserAgents)
