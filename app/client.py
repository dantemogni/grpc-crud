import grpc
import book_pb2, book_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = book_pb2_grpc.BookStub(channel)
        book = stub.CreateBook(book_pb2.BookRequest(name = "Prueba", 
                                                    genre = "Genero Prueba",
                                                    pages = 50,
                                                    author = "Autor prueba",
                                                    isbn = "isbn prueba"))
    print(book)

if __name__ == '__main__':
    run()