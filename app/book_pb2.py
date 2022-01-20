# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: book.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='book.proto',
  package='libraryPackage',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nbook.proto\x12\x0elibraryPackage\"\x06\n\x04void\"`\n\x08\x42ookItem\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05genre\x18\x03 \x01(\t\x12\r\n\x05pages\x18\x04 \x01(\x05\x12\x0e\n\x06\x61uthor\x18\x05 \x01(\t\x12\x0c\n\x04isbn\x18\x06 \x01(\t\"W\n\x0b\x42ookRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05genre\x18\x02 \x01(\t\x12\r\n\x05pages\x18\x03 \x01(\x05\x12\x0e\n\x06\x61uthor\x18\x04 \x01(\t\x12\x0c\n\x04isbn\x18\x05 \x01(\t\"8\n\tBookItems\x12+\n\tbookItems\x18\x01 \x03(\x0b\x32\x18.libraryPackage.BookItem2\x8f\x01\n\x04\x42ook\x12\x45\n\nCreateBook\x12\x1b.libraryPackage.BookRequest\x1a\x18.libraryPackage.BookItem\"\x00\x12@\n\tListBooks\x12\x14.libraryPackage.void\x1a\x19.libraryPackage.BookItems\"\x00\x30\x01\x62\x06proto3'
)




_VOID = _descriptor.Descriptor(
  name='void',
  full_name='libraryPackage.void',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=36,
)


_BOOKITEM = _descriptor.Descriptor(
  name='BookItem',
  full_name='libraryPackage.BookItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='libraryPackage.BookItem.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='libraryPackage.BookItem.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='genre', full_name='libraryPackage.BookItem.genre', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pages', full_name='libraryPackage.BookItem.pages', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='author', full_name='libraryPackage.BookItem.author', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isbn', full_name='libraryPackage.BookItem.isbn', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=134,
)


_BOOKREQUEST = _descriptor.Descriptor(
  name='BookRequest',
  full_name='libraryPackage.BookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='libraryPackage.BookRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='genre', full_name='libraryPackage.BookRequest.genre', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pages', full_name='libraryPackage.BookRequest.pages', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='author', full_name='libraryPackage.BookRequest.author', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isbn', full_name='libraryPackage.BookRequest.isbn', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=223,
)


_BOOKITEMS = _descriptor.Descriptor(
  name='BookItems',
  full_name='libraryPackage.BookItems',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bookItems', full_name='libraryPackage.BookItems.bookItems', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=281,
)

_BOOKITEMS.fields_by_name['bookItems'].message_type = _BOOKITEM
DESCRIPTOR.message_types_by_name['void'] = _VOID
DESCRIPTOR.message_types_by_name['BookItem'] = _BOOKITEM
DESCRIPTOR.message_types_by_name['BookRequest'] = _BOOKREQUEST
DESCRIPTOR.message_types_by_name['BookItems'] = _BOOKITEMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

void = _reflection.GeneratedProtocolMessageType('void', (_message.Message,), {
  'DESCRIPTOR' : _VOID,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:libraryPackage.void)
  })
_sym_db.RegisterMessage(void)

BookItem = _reflection.GeneratedProtocolMessageType('BookItem', (_message.Message,), {
  'DESCRIPTOR' : _BOOKITEM,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:libraryPackage.BookItem)
  })
_sym_db.RegisterMessage(BookItem)

BookRequest = _reflection.GeneratedProtocolMessageType('BookRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOKREQUEST,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:libraryPackage.BookRequest)
  })
_sym_db.RegisterMessage(BookRequest)

BookItems = _reflection.GeneratedProtocolMessageType('BookItems', (_message.Message,), {
  'DESCRIPTOR' : _BOOKITEMS,
  '__module__' : 'book_pb2'
  # @@protoc_insertion_point(class_scope:libraryPackage.BookItems)
  })
_sym_db.RegisterMessage(BookItems)



_BOOK = _descriptor.ServiceDescriptor(
  name='Book',
  full_name='libraryPackage.Book',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=284,
  serialized_end=427,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateBook',
    full_name='libraryPackage.Book.CreateBook',
    index=0,
    containing_service=None,
    input_type=_BOOKREQUEST,
    output_type=_BOOKITEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListBooks',
    full_name='libraryPackage.Book.ListBooks',
    index=1,
    containing_service=None,
    input_type=_VOID,
    output_type=_BOOKITEMS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOOK)

DESCRIPTOR.services_by_name['Book'] = _BOOK

# @@protoc_insertion_point(module_scope)
