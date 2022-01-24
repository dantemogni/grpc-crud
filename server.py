from concurrent import futures
from email import message
import logging
import grpc
from pymongo import MongoClient
from pymongo import ReturnDocument
from bson.json_util import dumps
from bson.objectid import ObjectId
from google.protobuf.json_format import Parse
from google.protobuf.json_format import MessageToDict
from generated import library_pb2 as lib_object, library_pb2_grpc as lib_service
import exceptions.library_exceptions as lib_ex

class LibraryServicer(lib_service.LibraryServicer):
    def __init__(self):
        # inits the db
        self.client = MongoClient('mongodb://root:password@localhost:27017')
        self.db = self.client.library

    def AddBook(self, request, context):
        print("Received 'AddBook' request")  # debug

        if not request.title:
            raise lib_ex.NoTitleProvided
        if not request.genre:
            raise lib_ex.NoGenreProvided
        if not request.pages:
            raise lib_ex.NoPagesProvided
        if not request.author:
            raise lib_ex.NoAuthorProvided
        if not request.year:
            raise lib_ex.NoYearProvided
        if not request.isbn:
            raise lib_ex.NoIsbnProvided

        # parses gRCP class to JSON for saving it in the db
        book_to_add = MessageToDict(request)
        # obtains ENUM value of genre
        book_to_add['genre'] = lib_object.BookGenre.Value(
            request.genre.upper())

        # inserts to db & saves the generated id by mongo
        self.db.books.insert_one(book_to_add)

        # returns gRPC object with the parsed data. Optional
        book_to_add['_id'] = str(book_to_add['_id'])
        return_value = Parse(dumps(book_to_add), lib_object.BookItem())

        return return_value

    def EditBook(self, request, context):
        # parses gRCP class to JSON for saving it in the db
        book_to_edit = MessageToDict(request.book)
        # obtains ENUM value of genre
        genre_value = lib_object.BookGenre.Value(book_to_edit['genre'].upper())

        # updates and returns the updated value
        updated_book = self.db.books.find_one_and_update(
            {"_id": ObjectId(request.id)},
            {"$set": {
                'title': book_to_edit['title'],
                'genre': genre_value,
                'pages': book_to_edit['pages'],
                'author': book_to_edit['author'],
                'year': book_to_edit['year'],
                'isbn': book_to_edit['isbn']}},
            return_document=ReturnDocument.AFTER)

        # returns gRPC object with the parsed data. Optional
        updated_book['_id'] = str(updated_book['_id'])
        updated_book = Parse(dumps(updated_book), lib_object.BookItem())

        return updated_book

    def DeleteBook(self, request, context):
        print("Received 'DeleteBook' request")  # debug
        self.db.books.find_one_and_delete({"_id": ObjectId(request.id)})
        return lib_object.void()  # gRPC needs a return value

    def GetBookById(self, request, context):
        print("Received 'GetBookById' request")  # debug
        book = self.db.books.find_one({"_id": ObjectId(request.id)})
        book['_id'] = str(book['_id'])
        return Parse(dumps(book), lib_object.BookItem())

    def GetBooks(self, request, context):
        print("Received 'GetBooks' request")  # debug
        for book in self.db.books.find():
            book['_id'] = str(book['_id'])
            yield Parse(dumps(book), lib_object.BookItem())


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
