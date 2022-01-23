from concurrent import futures
import logging
import grpc

from generated import library_pb2, library_pb2_grpc


class LibraryServicer(library_pb2_grpc.LibraryServicer):
    def AddBook(self, request, context):
        return library_pb2.BookItem(name = request.name,
                                 genre = request.genre,
                                 pages = request.pages,
                                 author = request.author,
                                 isbn = request.isbn)
    
    def ListBooks(self, request, context):
        for book in self.db: # TODO
            yield book


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    library_pb2_grpc.add_LibraryServicer_to_server(
        LibraryServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
