from concurrent import futures
import grpc
import os
import sample_service_pb2 as service_objects
import sample_service_pb2_grpc as service_stub


class SampleServiceImpl(service_stub.QuestionClassificationServicesServicer):

    def __init__(self):
        pass

    def getSampleQuestions(self, request, context):
        max_ques = request.limit
        print('received total limit of ', max_ques)
        data = [service_objects.QuestionDetails(question="Hello World {}".format(i), questionClass="test") for i in range(max_ques)]
        host = os.getenv('HOSTNAME', 'localhost')
        response = service_objects.GetQuestionsMessage(limit=max_ques, questionDetailsList=data, fromHost=host)
        print('responding with response limit of ', len(response.questionDetailsList))
        return response

    def streamSampleQuestions(self, request_iterator, context):
        for new_request in request_iterator:
            max_ques = new_request.limit
            print('received total limit of ', max_ques)
            data = [service_objects.QuestionDetails(question="Hello World {}".format(i), questionClass="test") for i in
                    range(max_ques)]
            host = os.getenv('HOSTNAME', 'localhost')
            response = service_objects.GetQuestionsMessage(limit=max_ques, questionDetailsList=data, fromHost=host)
            print('responding with response limit of ', len(response.questionDetailsList))
            yield response

    def getTaggedQuestions(self, request, context):
        pass


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    service_stub.add_QuestionClassificationServicesServicer_to_server(
        SampleServiceImpl(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print(server)
    server.wait_for_termination()
