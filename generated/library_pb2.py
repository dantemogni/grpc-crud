# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: library.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='library.proto',
  package='library',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rlibrary.proto\x12\x07library\"\x06\n\x04void\"\x84\x01\n\x08\x42ookItem\x12\x0b\n\x03_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12!\n\x05genre\x18\x03 \x01(\x0e\x32\x12.library.BookGenre\x12\r\n\x05pages\x18\x04 \x01(\x05\x12\x0e\n\x06\x61uthor\x18\x05 \x01(\t\x12\x0c\n\x04year\x18\x06 \x01(\x05\x12\x0c\n\x04isbn\x18\x07 \x01(\t\"f\n\x0b\x42ookRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\r\n\x05genre\x18\x02 \x01(\t\x12\r\n\x05pages\x18\x03 \x01(\x05\x12\x0e\n\x06\x61uthor\x18\x04 \x01(\t\x12\x0c\n\x04year\x18\x05 \x01(\x05\x12\x0c\n\x04isbn\x18\x06 \x01(\t\"A\n\x0f\x45\x64itBookRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\"\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x14.library.BookRequest\"1\n\tBookItems\x12$\n\tbookItems\x18\x01 \x01(\x0b\x32\x11.library.BookItem\"\x10\n\x02Id\x12\n\n\x02id\x18\x01 \x01(\t*\xef\x01\n\tBookGenre\x12\x08\n\x04NONE\x10\x00\x12\r\n\tADVENTURE\x10\x01\x12\n\n\x06\x41\x43TION\x10\x02\x12\x0c\n\x08\x43LASSICS\x10\x03\x12\x0b\n\x07MYSTERY\x10\x04\x12\x0b\n\x07ROMANCE\x10\x05\x12\x0e\n\nBIOGRAPHIC\x10\x06\x12\x0b\n\x07HISTORY\x10\x07\x12\n\n\x06\x45SSAYS\x10\x08\x12\n\n\x06POETRY\x10\t\x12\r\n\tSELF_HELP\x10\n\x12\n\n\x06\x43OMEDY\x10\x0b\x12\t\n\x05\x44RAMA\x10\x0c\x12\n\n\x06HORROR\x10\r\x12\n\n\x06SCI_FI\x10\x0e\x12\x0c\n\x08THRILLER\x10\x0f\x12\x07\n\x03WAR\x10\x10\x12\x0b\n\x07WESTERN\x10\x11\x32\x89\x02\n\x07Library\x12\x34\n\x07\x41\x64\x64\x42ook\x12\x14.library.BookRequest\x1a\x11.library.BookItem\"\x00\x12\x39\n\x08\x45\x64itBook\x12\x18.library.EditBookRequest\x1a\x11.library.BookItem\"\x00\x12*\n\nDeleteBook\x12\x0b.library.Id\x1a\r.library.void\"\x00\x12/\n\x0bGetBookById\x12\x0b.library.Id\x1a\x11.library.BookItem\"\x00\x12\x30\n\x08GetBooks\x12\r.library.void\x1a\x11.library.BookItem\"\x00\x30\x01\x62\x06proto3'
)

_BOOKGENRE = _descriptor.EnumDescriptor(
  name='BookGenre',
  full_name='library.BookGenre',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADVENTURE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLASSICS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MYSTERY', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROMANCE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BIOGRAPHIC', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HISTORY', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ESSAYS', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POETRY', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SELF_HELP', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMEDY', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DRAMA', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HORROR', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCI_FI', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='THRILLER', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WAR', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WESTERN', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=410,
  serialized_end=649,
)
_sym_db.RegisterEnumDescriptor(_BOOKGENRE)

BookGenre = enum_type_wrapper.EnumTypeWrapper(_BOOKGENRE)
NONE = 0
ADVENTURE = 1
ACTION = 2
CLASSICS = 3
MYSTERY = 4
ROMANCE = 5
BIOGRAPHIC = 6
HISTORY = 7
ESSAYS = 8
POETRY = 9
SELF_HELP = 10
COMEDY = 11
DRAMA = 12
HORROR = 13
SCI_FI = 14
THRILLER = 15
WAR = 16
WESTERN = 17



_VOID = _descriptor.Descriptor(
  name='void',
  full_name='library.void',
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
  serialized_start=26,
  serialized_end=32,
)


_BOOKITEM = _descriptor.Descriptor(
  name='BookItem',
  full_name='library.BookItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='_id', full_name='library.BookItem._id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='library.BookItem.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='genre', full_name='library.BookItem.genre', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pages', full_name='library.BookItem.pages', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='author', full_name='library.BookItem.author', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='library.BookItem.year', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isbn', full_name='library.BookItem.isbn', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=35,
  serialized_end=167,
)


_BOOKREQUEST = _descriptor.Descriptor(
  name='BookRequest',
  full_name='library.BookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='library.BookRequest.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='genre', full_name='library.BookRequest.genre', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pages', full_name='library.BookRequest.pages', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='author', full_name='library.BookRequest.author', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='library.BookRequest.year', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isbn', full_name='library.BookRequest.isbn', index=5,
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
  serialized_start=169,
  serialized_end=271,
)


_EDITBOOKREQUEST = _descriptor.Descriptor(
  name='EditBookRequest',
  full_name='library.EditBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='library.EditBookRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='book', full_name='library.EditBookRequest.book', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=273,
  serialized_end=338,
)


_BOOKITEMS = _descriptor.Descriptor(
  name='BookItems',
  full_name='library.BookItems',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bookItems', full_name='library.BookItems.bookItems', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=340,
  serialized_end=389,
)


_ID = _descriptor.Descriptor(
  name='Id',
  full_name='library.Id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='library.Id.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=391,
  serialized_end=407,
)

_BOOKITEM.fields_by_name['genre'].enum_type = _BOOKGENRE
_EDITBOOKREQUEST.fields_by_name['book'].message_type = _BOOKREQUEST
_BOOKITEMS.fields_by_name['bookItems'].message_type = _BOOKITEM
DESCRIPTOR.message_types_by_name['void'] = _VOID
DESCRIPTOR.message_types_by_name['BookItem'] = _BOOKITEM
DESCRIPTOR.message_types_by_name['BookRequest'] = _BOOKREQUEST
DESCRIPTOR.message_types_by_name['EditBookRequest'] = _EDITBOOKREQUEST
DESCRIPTOR.message_types_by_name['BookItems'] = _BOOKITEMS
DESCRIPTOR.message_types_by_name['Id'] = _ID
DESCRIPTOR.enum_types_by_name['BookGenre'] = _BOOKGENRE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

void = _reflection.GeneratedProtocolMessageType('void', (_message.Message,), {
  'DESCRIPTOR' : _VOID,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:library.void)
  })
_sym_db.RegisterMessage(void)

BookItem = _reflection.GeneratedProtocolMessageType('BookItem', (_message.Message,), {
  'DESCRIPTOR' : _BOOKITEM,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:library.BookItem)
  })
_sym_db.RegisterMessage(BookItem)

BookRequest = _reflection.GeneratedProtocolMessageType('BookRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOKREQUEST,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:library.BookRequest)
  })
_sym_db.RegisterMessage(BookRequest)

EditBookRequest = _reflection.GeneratedProtocolMessageType('EditBookRequest', (_message.Message,), {
  'DESCRIPTOR' : _EDITBOOKREQUEST,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:library.EditBookRequest)
  })
_sym_db.RegisterMessage(EditBookRequest)

BookItems = _reflection.GeneratedProtocolMessageType('BookItems', (_message.Message,), {
  'DESCRIPTOR' : _BOOKITEMS,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:library.BookItems)
  })
_sym_db.RegisterMessage(BookItems)

Id = _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), {
  'DESCRIPTOR' : _ID,
  '__module__' : 'library_pb2'
  # @@protoc_insertion_point(class_scope:library.Id)
  })
_sym_db.RegisterMessage(Id)



_LIBRARY = _descriptor.ServiceDescriptor(
  name='Library',
  full_name='library.Library',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=652,
  serialized_end=917,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddBook',
    full_name='library.Library.AddBook',
    index=0,
    containing_service=None,
    input_type=_BOOKREQUEST,
    output_type=_BOOKITEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EditBook',
    full_name='library.Library.EditBook',
    index=1,
    containing_service=None,
    input_type=_EDITBOOKREQUEST,
    output_type=_BOOKITEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteBook',
    full_name='library.Library.DeleteBook',
    index=2,
    containing_service=None,
    input_type=_ID,
    output_type=_VOID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBookById',
    full_name='library.Library.GetBookById',
    index=3,
    containing_service=None,
    input_type=_ID,
    output_type=_BOOKITEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetBooks',
    full_name='library.Library.GetBooks',
    index=4,
    containing_service=None,
    input_type=_VOID,
    output_type=_BOOKITEM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LIBRARY)

DESCRIPTOR.services_by_name['Library'] = _LIBRARY

# @@protoc_insertion_point(module_scope)
