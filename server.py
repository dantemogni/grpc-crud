from concurrent import futures
import logging
import grpc

from generated import library_pb2, library_pb2_grpc

library_demo = []

class LibraryServiceServicer(library_pb2_grpc.LibraryServiceServicer):
    def AddBook(self, request, context):
        # TODO: calcular el id 

        print("Received 'AddBook' request") #debug

        genre_value = library_pb2.BookGenre.Value(request.genre.upper())
        
        book_to_add = library_pb2.BookItem(
                        id = 1,
                        title = request.title,
                        genre = genre_value,
                        pages = request.pages,
                        author = request.author,
                        year = request.year,
                        isbn = request.isbn
                      )

        library_demo.append(book_to_add)

        return book_to_add
    
    def GetBooks(self, request, context):
        print("Received 'GetBooks' request") #debug
        for book in library_demo:
            yield library_pb2.BookItem(
                id = book.id,
                title = book.title,
                genre = book.genre,
                pages = book.pages,
                author = book.author,
                year = book.year,
                isbn = book.isbn
            )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    library_pb2_grpc.add_LibraryServiceServicer_to_server(
        LibraryServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    print("Server started in port: 50051") # debug

    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
