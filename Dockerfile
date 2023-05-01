FROM apache/spark-py:latest

ADD ./jobs/ ./jobs/

ADD ./utilities ./utilities

ADD ./test/data/site-visits/ ./test/data/site-visits/
