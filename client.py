import logging
import grpc

from generated import library_pb2, library_pb2_grpc

def library_add_book(stub):
    book = stub.AddBook(library_pb2.BookRequest(name = "Prueba", 
                                                    genre = "Genero Prueba",
                                                    pages = 50,
                                                    author = "Autor prueba",
                                                    isbn = "isbn prueba"))
    print(book)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = library_pb2_grpc.LibraryStub(channel)
        library_add_book(stub)

if __name__ == '__main__':
    logging.basicConfig()
    run()