# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: udpa/annotations/migrate.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='udpa/annotations/migrate.proto',
  package='udpa.annotations',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1eudpa/annotations/migrate.proto\x12\x10udpa.annotations\x1a google/protobuf/descriptor.proto\"#\n\x11MigrateAnnotation\x12\x0e\n\x06rename\x18\x01 \x01(\t\"A\n\x16\x46ieldMigrateAnnotation\x12\x0e\n\x06rename\x18\x01 \x01(\t\x12\x17\n\x0foneof_promotion\x18\x02 \x01(\t\"0\n\x15\x46ileMigrateAnnotation\x12\x17\n\x0fmove_to_package\x18\x02 \x01(\t:`\n\x0fmessage_migrate\x12\x1f.google.protobuf.MessageOptions\x18\x8e\xe3\xffQ \x01(\x0b\x32#.udpa.annotations.MigrateAnnotation:a\n\rfield_migrate\x12\x1d.google.protobuf.FieldOptions\x18\x8e\xe3\xffQ \x01(\x0b\x32(.udpa.annotations.FieldMigrateAnnotation:Z\n\x0c\x65num_migrate\x12\x1c.google.protobuf.EnumOptions\x18\x8e\xe3\xffQ \x01(\x0b\x32#.udpa.annotations.MigrateAnnotation:e\n\x12\x65num_value_migrate\x12!.google.protobuf.EnumValueOptions\x18\x8e\xe3\xffQ \x01(\x0b\x32#.udpa.annotations.MigrateAnnotation:^\n\x0c\x66ile_migrate\x12\x1c.google.protobuf.FileOptions\x18\x8e\xe3\xffQ \x01(\x0b\x32\'.udpa.annotations.FileMigrateAnnotationb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


MESSAGE_MIGRATE_FIELD_NUMBER = 171962766
message_migrate = _descriptor.FieldDescriptor(
  name='message_migrate', full_name='udpa.annotations.message_migrate', index=0,
  number=171962766, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
FIELD_MIGRATE_FIELD_NUMBER = 171962766
field_migrate = _descriptor.FieldDescriptor(
  name='field_migrate', full_name='udpa.annotations.field_migrate', index=1,
  number=171962766, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
ENUM_MIGRATE_FIELD_NUMBER = 171962766
enum_migrate = _descriptor.FieldDescriptor(
  name='enum_migrate', full_name='udpa.annotations.enum_migrate', index=2,
  number=171962766, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
ENUM_VALUE_MIGRATE_FIELD_NUMBER = 171962766
enum_value_migrate = _descriptor.FieldDescriptor(
  name='enum_value_migrate', full_name='udpa.annotations.enum_value_migrate', index=3,
  number=171962766, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
FILE_MIGRATE_FIELD_NUMBER = 171962766
file_migrate = _descriptor.FieldDescriptor(
  name='file_migrate', full_name='udpa.annotations.file_migrate', index=4,
  number=171962766, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)


_MIGRATEANNOTATION = _descriptor.Descriptor(
  name='MigrateAnnotation',
  full_name='udpa.annotations.MigrateAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rename', full_name='udpa.annotations.MigrateAnnotation.rename', index=0,
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
  serialized_start=86,
  serialized_end=121,
)


_FIELDMIGRATEANNOTATION = _descriptor.Descriptor(
  name='FieldMigrateAnnotation',
  full_name='udpa.annotations.FieldMigrateAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rename', full_name='udpa.annotations.FieldMigrateAnnotation.rename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='oneof_promotion', full_name='udpa.annotations.FieldMigrateAnnotation.oneof_promotion', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=123,
  serialized_end=188,
)


_FILEMIGRATEANNOTATION = _descriptor.Descriptor(
  name='FileMigrateAnnotation',
  full_name='udpa.annotations.FileMigrateAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='move_to_package', full_name='udpa.annotations.FileMigrateAnnotation.move_to_package', index=0,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=190,
  serialized_end=238,
)

DESCRIPTOR.message_types_by_name['MigrateAnnotation'] = _MIGRATEANNOTATION
DESCRIPTOR.message_types_by_name['FieldMigrateAnnotation'] = _FIELDMIGRATEANNOTATION
DESCRIPTOR.message_types_by_name['FileMigrateAnnotation'] = _FILEMIGRATEANNOTATION
DESCRIPTOR.extensions_by_name['message_migrate'] = message_migrate
DESCRIPTOR.extensions_by_name['field_migrate'] = field_migrate
DESCRIPTOR.extensions_by_name['enum_migrate'] = enum_migrate
DESCRIPTOR.extensions_by_name['enum_value_migrate'] = enum_value_migrate
DESCRIPTOR.extensions_by_name['file_migrate'] = file_migrate
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MigrateAnnotation = _reflection.GeneratedProtocolMessageType('MigrateAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _MIGRATEANNOTATION,
  '__module__' : 'udpa.annotations.migrate_pb2'
  # @@protoc_insertion_point(class_scope:udpa.annotations.MigrateAnnotation)
  })
_sym_db.RegisterMessage(MigrateAnnotation)

FieldMigrateAnnotation = _reflection.GeneratedProtocolMessageType('FieldMigrateAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _FIELDMIGRATEANNOTATION,
  '__module__' : 'udpa.annotations.migrate_pb2'
  # @@protoc_insertion_point(class_scope:udpa.annotations.FieldMigrateAnnotation)
  })
_sym_db.RegisterMessage(FieldMigrateAnnotation)

FileMigrateAnnotation = _reflection.GeneratedProtocolMessageType('FileMigrateAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _FILEMIGRATEANNOTATION,
  '__module__' : 'udpa.annotations.migrate_pb2'
  # @@protoc_insertion_point(class_scope:udpa.annotations.FileMigrateAnnotation)
  })
_sym_db.RegisterMessage(FileMigrateAnnotation)

message_migrate.message_type = _MIGRATEANNOTATION
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(message_migrate)
field_migrate.message_type = _FIELDMIGRATEANNOTATION
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field_migrate)
enum_migrate.message_type = _MIGRATEANNOTATION
google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(enum_migrate)
enum_value_migrate.message_type = _MIGRATEANNOTATION
google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(enum_value_migrate)
file_migrate.message_type = _FILEMIGRATEANNOTATION
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(file_migrate)

# @@protoc_insertion_point(module_scope)