import grpc

import proto_generated.sample_service_pb2 as service_objects
import proto_generated.sample_service_pb2_grpc as service_stub


def run():
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = service_stub.QuestionClassificationServicesStub(channel)
        request = service_objects.GetQuestionsMessage(limit=2, questionDetailsList=[])
        response = stub.getSampleQuestions(request)
        print(response)


if __name__ == "__main__":
    run()
