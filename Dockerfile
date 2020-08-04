FROM python:3.7.8-slim-buster

ADD qc-services /qc-services
RUN pip install -r qc-services/requirements.txt
RUN rm -r /root/.cache
WORKDIR /qc-services