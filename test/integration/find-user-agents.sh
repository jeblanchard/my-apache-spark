docker exec my-apache-spark pwd

docker cp ./test my-apache-spark:./opt/spark/work-dir

dataPath="./test/data/site-visits"
scriptPath="./jobs/collect_user_agents.py"
cmd="../bin/spark-submit $scriptPath $dataPath"

docker exec my-apache-spark ls

docker exec my-apache-spark $cmd
