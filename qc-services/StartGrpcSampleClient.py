import grpc
import time
import os

import sample_service_pb2 as service_objects
import sample_service_pb2_grpc as service_stub


def run(channel):
    stub = service_stub.QuestionClassificationServicesStub(channel)
    request = service_objects.GetQuestionsMessage(limit=2, questionDetailsList=[])
    response = stub.getSampleQuestions(request)
    print('unary qc list length {}- from host {}'.format(len(response.questionDetailsList), response.fromHost))


def run_streams(channel):
    def request_generator():
        for i in range(5):
            request = service_objects.GetQuestionsMessage(limit=i, questionDetailsList=[])
            yield request

    stub = service_stub.QuestionClassificationServicesStub(channel)
    gen_func = request_generator()
    response_list = stub.streamSampleQuestions(gen_func)
    for response in response_list:
        print('streams qc list length {}- from host {}'.format(len(response.questionDetailsList), response.fromHost))


if __name__ == "__main__":
    host = os.getenv('QC-SERVER-DNS', '127.0.0.1')
    port = os.getenv('QC-SERVER-PORT', '50051')
    print('connecting to host ', host)
    with grpc.insecure_channel(host+':'+port) as channel:
        while True:
            run_streams(channel)
            run(channel)
            time.sleep(1.5)
