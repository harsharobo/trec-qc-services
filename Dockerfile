FROM python:3.7.8-alpine3.12

ADD trec-qc-services /trec-qc-services
RUN pip install -r requirements.txt
RUN cd service

EXPOSE 50051
CMD ["python","StartGrpcSampleService.py"]