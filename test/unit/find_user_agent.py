import sys

sys.path.append('C:\\Users\\blanc\\personal-projects\\my-apache-spark')
from utilities.requests import find_user_agent

correct_user_agent = "GoogleHC/1.0"
request_file_path = "./test/data/site-visits/site-visit-1682453805068-84.txt"

textFile = open(request_file_path, mode='rt', newline='\n')
text = textFile.read()
textFile.close()

filename_content_tuple = (request_file_path, text)

actual_user_agent = find_user_agent(filename_content_tuple)

if actual_user_agent == correct_user_agent:
    print("Test passed.")
else:
    raise Exception(f"Test failed.\nActual: {actual_user_agent}\nCorrect: {correct_user_agent}")
