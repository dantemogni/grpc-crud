from concurrent import futures
import logging
import grpc

import book_pb2_grpc, book_pb2

class BookServicer(book_pb2_grpc.BookServicer):
    def CreateBook(self, request, context):
        return book_pb2.BookItem(name = request.name,
                                 genre = request.genre,
                                 pages = request.pages,
                                 author = request.author,
                                 isbn = request.isbn)
    
    def ListBooks(self, request, context):
        for book in self.db: # TODO
            yield book


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_pb2_grpc.add_BookServicer_to_server(
        BookServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
