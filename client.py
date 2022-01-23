import logging
import grpc

from generated import library_pb2, library_pb2_grpc

def library_add_book(stub):
    book = stub.AddBook(library_pb2.BookRequest(
                                            title = "Las Peripecias del Tonto Enojado", 
                                            genre = "thriller",
                                            pages = 315,
                                            author = "Autor prueba",
                                            year = 2006,
                                            isbn = "978-987-25620-2-1"
                                            ))
    print(book) # guardar en DB


def library_get_books(stub):
    responses = stub.GetBooks(library_pb2.void()) # returns a stream
    for res in responses:
        print(res)

# def library_edit_book(stub):
#     book = stub.EditBook(library_pb2.EditBookRequest(
#                                                     id = "1",
#                                                     BookRequest = library_pb2.BookRequest(
#                                                         name = "Nombre editado",
#                                                         genre = "genero editado"
#                                                     )))
#     print(book) #guardar en DB


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = library_pb2_grpc.LibraryServiceStub(channel)
        library_add_book(stub)
        library_get_books(stub)

if __name__ == '__main__':
    logging.basicConfig()
    run()