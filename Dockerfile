FROM python:3.7.8-slim-buster

ADD trec-qc-services /trec-qc-services
RUN pip install -r trec-qc-services/requirements.txt
RUN rm -r /root/.cache
WORKDIR /trec-qc-services

EXPOSE 50051