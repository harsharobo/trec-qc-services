import grpc
import time
import os

import proto_generated.sample_service_pb2 as service_objects
import proto_generated.sample_service_pb2_grpc as service_stub


def run(channel):
    stub = service_stub.QuestionClassificationServicesStub(channel)
    request = service_objects.GetQuestionsMessage(limit=2, questionDetailsList=[])
    response = stub.getSampleQuestions(request)
    print(response)


if __name__ == "__main__":
    host = os.getenv('QC-SERVER-DNS', '127.0.0.1')
    print('connecting to host ', host)
    with grpc.insecure_channel(host+':9005') as channel:
        while True:
            run(channel)
            time.sleep(1.5)
