FROM apache/spark-py:latest

COPY ./sample.py ./sample.py

COPY test/data/* ./data/*
