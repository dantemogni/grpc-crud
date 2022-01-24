import logging
import grpc

from generated import library_pb2 as lib_object, library_pb2_grpc as lib_service

def library_add_book(stub):
    book = stub.AddBook(lib_object.BookRequest(
        title="Las Peripecias del Tonto Enojado",
        genre="thriller",
        pages=315,
        author="Autor prueba",
        year=2006,
        isbn="978-987-25620-2-1"
    ))
    print(book)  # guardar en DB


def library_edit_book(stub):
    book = stub.EditBook(lib_object.EditBookRequest(
        id="61eed54b885249342ac8228e",
        book=lib_object.BookRequest(
            title="Las Aventuras del Tonto Enojado",
            genre="drama",
            pages=315,
            author="Autor prueba",
            year=2006,
            isbn="978-987-25620-2-1"
        )
    ))
    print(book)


def library_delete_book(stub):
    stub.DeleteBook(lib_object.Id(id="61eee7d4144497a3400d0175"))


def library_get_book_by_id(stub):
    book = stub.GetBookById(lib_object.Id(id="61eee6eb5d4f9c3d44fcea12"))
    print(book)


def library_get_books(stub):
    responses = stub.GetBooks(lib_object.void())  # returns a stream
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
        stub = lib_service.LibraryStub(channel)
        print("------------- ADD BOOK & PRINT")
        library_add_book(stub)
        print("------------- EDIT BOOK & PRINT")
        library_edit_book(stub)
        print("------------- DELETE BOOK ID[1]")
        library_delete_book(stub)
        print("------------- GET BOOK BY ID[61eee6eb5d4f9c3d44fcea12]")
        library_get_book_by_id(stub)
        print("------------- YIELD ALL BOOKS")
        library_get_books(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()
