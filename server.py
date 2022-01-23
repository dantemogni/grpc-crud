from concurrent import futures
import logging
from turtle import title
import grpc

from generated import library_pb2 as lib_object, library_pb2_grpc as lib_service

# DATA LIST FOR DEMO PURPOSES ONLY
library_demo = []

#TODO: validate data, exception handling

class LibraryServicer(lib_service.LibraryServicer):
    # def __init__(self):
    #     read database

    def AddBook(self, request, context):
        print("Received 'AddBook' request")  # debug

        # calculates id based on the last item of the list, plus one
        calculated_id = (library_demo[-1].id + 1) if library_demo else 1

        # TODO: throw exception
        if request.book.title:
            print("Please provide a title")
        if request.book.genre:
            print("Please provide a genre")
        if request.book.pages:
            print("Please provide a page number")
        if request.book.author:
            print("Please provide an author")
        if request.book.year:
            print("Please provide a year")
        if request.book.isbn:
            print("Please provide an isbn")

        book_to_add = lib_object.BookItem(
            id=calculated_id,
            title=request.title,
            genre=lib_object.BookGenre.Value(request.genre.upper()),
            pages=request.pages,
            author=request.author,
            year=request.year,
            isbn=request.isbn
        )

        library_demo.append(book_to_add)

        return book_to_add

    def EditBook(self, request, context):
        i = 0
        book_to_edit = None

        while (book_to_edit == None and i < len(library_demo)):
            if(library_demo[i].id == request.id):
                book_to_edit = library_demo[i]
            i += 1

        # only modifies values that are passed by
        if request.book.title:
            book_to_edit.title = request.book.title
        if request.book.genre:
            book_to_edit.genre = lib_object.BookGenre.Value(
                request.genre.upper())
        if request.book.pages:
            book_to_edit.pages = request.book.pages
        if request.book.author:
            book_to_edit.author = request.book.author
        if request.book.year:
            book_to_edit.year = request.book.year
        if request.book.isbn:
            book_to_edit.isbn = request.book.isbn

        return book_to_edit

    def DeleteBook(self, request, context):
        print("Received 'DeleteBook' request")  # debug

        for book in library_demo:
            if book.id == request.id:
                library_demo.remove(book)
                return lib_object.void()

    def GetBookById(self, request, context):
        print("Received 'GetBookById' request")  # debug

        for book in library_demo:
            if book.id == request.id:
                return book
        return None #TODO: exception

    def GetBooks(self, request, context):
        print("Received 'GetBooks' request")  # debug
        for book in library_demo:
            yield book


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    lib_service.add_LibraryServicer_to_server(
        LibraryServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    print("Server started in port: 50051")  # debug

    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
