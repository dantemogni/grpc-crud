import logging
import grpc

from generated import library_pb2 as lib_object, library_pb2_grpc as lib_service

def demo_add_many(stub):
    stub.AddBook(lib_object.BookRequest(
        title="El Principito",
        genre="CLASSICS",
        pages=96,
        author="Antoine de Saint-Exupéry",
        year=1946,
        isbn="978-987-25620-2-1"
    ))
    stub.AddBook(lib_object.BookRequest(
        title="Fahrenheit 451",
        genre="SCI_FI",
        pages=215,
        author="Ray Bradbury",
        year=1953,
        isbn="978-987-25620-2-1"
    ))
    stub.AddBook(lib_object.BookRequest(
        title="The Lord of the Rings",
        genre="adventure",
        pages=1137,
        author="J. R. R. Tolkien",
        year=1954,
        isbn="978-987-25620-2-1"
    ))
    stub.AddBook(lib_object.BookRequest(
        title="Moby Dick",
        genre="classics",
        pages=823,
        author="Herman Melville",
        year=1854,
        isbn="978-987-25620-2-1"
    ))
    stub.AddBook(lib_object.BookRequest(
        title="The Handmaid's Tale",
        genre="drama",
        pages=311,
        author="Margaret Atwoodutor prueba",
        year=1985,
        isbn="978-987-25620-2-1"
    ))
    stub.AddBook(lib_object.BookRequest(
        title="A Clockwork Orange",
        genre="SCI_FI",
        pages=200,
        author="Anthony Burgess",
        year=1962,
        isbn="978-987-25620-2-1"
    ))
    stub.AddBook(lib_object.BookRequest(
        title="Divina comedia",
        genre="classics",
        pages=806,
        author="Dante Alighieri",
        year=1472,
        isbn="978-987-25620-2-1"
    ))
    stub.AddBook(lib_object.BookRequest(
        title="Rebelión en la granja",
        genre="classics",
        pages=86,
        author="George Orwell",
        year=1945,
        isbn="978-987-25620-2-1"
    ))

def library_add_book(stub):
    book = stub.AddBook(lib_object.BookRequest(
        title="Las Peripecias del Tonto Enojado",
        genre="drama",
        pages=315,
        author="Autor prueba",
        year=2006,
        isbn="978-987-25620-2-1"
    ))
    print(book)


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


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = lib_service.LibraryStub(channel)

        #--------- demo purporses ----------------------

        # print("------------- INSERTS MANY ITEMS")
        # demo_add_many(stub)

        # print("------------- ADD BOOK & PRINT")
        #library_add_book(stub)

        # print("------------- EDIT BOOK & PRINT")
        # library_edit_book(stub)

        # print("------------- DELETE BOOK ID[1]")
        # library_delete_book(stub)

        # print("------------- GET BOOK BY ID[61eee6eb5d4f9c3d44fcea12]")
        # library_get_book_by_id(stub)

        print("------------- YIELD ALL BOOKS")
        library_get_books(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()
