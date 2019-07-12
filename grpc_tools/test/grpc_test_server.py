import time
import grpc
import hello_pb2
import hello_pb2_grpc

from concurrent import futures



class Greeper(hello_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        print(request, context.__dict__)
        return hello_pb2.HelloReply(message='Hello, ' + request.name + ' times ' + str(request.qw))


    def SayHelloAgain(self, request, context):
        print(request, context)
        return hello_pb2.HelloReply(message='Hello ' + request.name + ' again')


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeper(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)