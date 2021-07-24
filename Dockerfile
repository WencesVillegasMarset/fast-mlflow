FROM python:3.8.5-slim-buster
RUN pip install mlflow==1.19.0 boto3 psycopg2-binary
