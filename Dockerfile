FROM apache/spark-py:latest

COPY jobs/collect_user_agents.py ./sample.py

COPY test/data/site-visits/ ./
