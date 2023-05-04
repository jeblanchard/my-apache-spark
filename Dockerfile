FROM apache/spark-py:latest

ADD ./jobs/ ./jobs/

ADD ./utilities ./utilities

# We do this to give us sufficient file system permissions.
USER 0
