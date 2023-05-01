FROM apache/spark-py:latest

ADD ./jobs/ ./jobs/

ADD ./utilities ./utilities
