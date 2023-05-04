docker exec my-apache-spark pwd

docker cp ./test my-apache-spark:./opt/spark/work-dir

inputDir="./test/data/in/site-visits"
outputFilename="./test/data/out/user_agents.csv"
pyJobFilename="./jobs/collect_user_agents.py"

cmd="../bin/spark-submit $pyJobFilename $inputDir $outputFilename"

docker exec my-apache-spark $cmd

outputFilenameForCp="./opt/spark/work-dir/test/data/out/user_agents.csv"
docker cp my-apache-spark:$outputFilenameForCp $outputFilename

validatorFilename="./test/src/check_user_agent_csv.py"

py $validatorFilename $outputFilename
