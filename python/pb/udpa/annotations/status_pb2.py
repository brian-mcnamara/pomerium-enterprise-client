# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: udpa/annotations/status.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='udpa/annotations/status.proto',
  package='udpa.annotations',
  syntax='proto3',
  serialized_options=b'Z\"github.com/cncf/xds/go/annotations',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1dudpa/annotations/status.proto\x12\x10udpa.annotations\x1a google/protobuf/descriptor.proto\"t\n\x10StatusAnnotation\x12\x18\n\x10work_in_progress\x18\x01 \x01(\x08\x12\x46\n\x16package_version_status\x18\x02 \x01(\x0e\x32&.udpa.annotations.PackageVersionStatus*]\n\x14PackageVersionStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x46ROZEN\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12 \n\x1cNEXT_MAJOR_VERSION_CANDIDATE\x10\x03:X\n\x0b\x66ile_status\x12\x1c.google.protobuf.FileOptions\x18\x87\x80\x99j \x01(\x0b\x32\".udpa.annotations.StatusAnnotationB$Z\"github.com/cncf/xds/go/annotationsb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])

_PACKAGEVERSIONSTATUS = _descriptor.EnumDescriptor(
  name='PackageVersionStatus',
  full_name='udpa.annotations.PackageVersionStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FROZEN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NEXT_MAJOR_VERSION_CANDIDATE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=203,
  serialized_end=296,
)
_sym_db.RegisterEnumDescriptor(_PACKAGEVERSIONSTATUS)

PackageVersionStatus = enum_type_wrapper.EnumTypeWrapper(_PACKAGEVERSIONSTATUS)
UNKNOWN = 0
FROZEN = 1
ACTIVE = 2
NEXT_MAJOR_VERSION_CANDIDATE = 3

FILE_STATUS_FIELD_NUMBER = 222707719
file_status = _descriptor.FieldDescriptor(
  name='file_status', full_name='udpa.annotations.file_status', index=0,
  number=222707719, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)


_STATUSANNOTATION = _descriptor.Descriptor(
  name='StatusAnnotation',
  full_name='udpa.annotations.StatusAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='work_in_progress', full_name='udpa.annotations.StatusAnnotation.work_in_progress', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='package_version_status', full_name='udpa.annotations.StatusAnnotation.package_version_status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=85,
  serialized_end=201,
)

_STATUSANNOTATION.fields_by_name['package_version_status'].enum_type = _PACKAGEVERSIONSTATUS
DESCRIPTOR.message_types_by_name['StatusAnnotation'] = _STATUSANNOTATION
DESCRIPTOR.enum_types_by_name['PackageVersionStatus'] = _PACKAGEVERSIONSTATUS
DESCRIPTOR.extensions_by_name['file_status'] = file_status
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatusAnnotation = _reflection.GeneratedProtocolMessageType('StatusAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _STATUSANNOTATION,
  '__module__' : 'udpa.annotations.status_pb2'
  # @@protoc_insertion_point(class_scope:udpa.annotations.StatusAnnotation)
  })
_sym_db.RegisterMessage(StatusAnnotation)

file_status.message_type = _STATUSANNOTATION
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(file_status)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
