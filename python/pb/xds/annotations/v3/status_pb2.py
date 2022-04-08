# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xds/annotations/v3/status.proto
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
  name='xds/annotations/v3/status.proto',
  package='xds.annotations.v3',
  syntax='proto3',
  serialized_options=b'Z)github.com/cncf/xds/go/xds/annotations/v3',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fxds/annotations/v3/status.proto\x12\x12xds.annotations.v3\x1a google/protobuf/descriptor.proto\"0\n\x14\x46ileStatusAnnotation\x12\x18\n\x10work_in_progress\x18\x01 \x01(\x08\"3\n\x17MessageStatusAnnotation\x12\x18\n\x10work_in_progress\x18\x01 \x01(\x08\"1\n\x15\x46ieldStatusAnnotation\x12\x18\n\x10work_in_progress\x18\x01 \x01(\x08\"v\n\x10StatusAnnotation\x12\x18\n\x10work_in_progress\x18\x01 \x01(\x08\x12H\n\x16package_version_status\x18\x02 \x01(\x0e\x32(.xds.annotations.v3.PackageVersionStatus*]\n\x14PackageVersionStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x46ROZEN\x10\x01\x12\n\n\x06\x41\x43TIVE\x10\x02\x12 \n\x1cNEXT_MAJOR_VERSION_CANDIDATE\x10\x03:^\n\x0b\x66ile_status\x12\x1c.google.protobuf.FileOptions\x18\xea\xc8\x94l \x01(\x0b\x32(.xds.annotations.v3.FileStatusAnnotation:g\n\x0emessage_status\x12\x1f.google.protobuf.MessageOptions\x18\xea\xc8\x94l \x01(\x0b\x32+.xds.annotations.v3.MessageStatusAnnotation:a\n\x0c\x66ield_status\x12\x1d.google.protobuf.FieldOptions\x18\xea\xc8\x94l \x01(\x0b\x32).xds.annotations.v3.FieldStatusAnnotationB+Z)github.com/cncf/xds/go/xds/annotations/v3b\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])

_PACKAGEVERSIONSTATUS = _descriptor.EnumDescriptor(
  name='PackageVersionStatus',
  full_name='xds.annotations.v3.PackageVersionStatus',
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
  serialized_start=363,
  serialized_end=456,
)
_sym_db.RegisterEnumDescriptor(_PACKAGEVERSIONSTATUS)

PackageVersionStatus = enum_type_wrapper.EnumTypeWrapper(_PACKAGEVERSIONSTATUS)
UNKNOWN = 0
FROZEN = 1
ACTIVE = 2
NEXT_MAJOR_VERSION_CANDIDATE = 3

FILE_STATUS_FIELD_NUMBER = 226829418
file_status = _descriptor.FieldDescriptor(
  name='file_status', full_name='xds.annotations.v3.file_status', index=0,
  number=226829418, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
MESSAGE_STATUS_FIELD_NUMBER = 226829418
message_status = _descriptor.FieldDescriptor(
  name='message_status', full_name='xds.annotations.v3.message_status', index=1,
  number=226829418, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
FIELD_STATUS_FIELD_NUMBER = 226829418
field_status = _descriptor.FieldDescriptor(
  name='field_status', full_name='xds.annotations.v3.field_status', index=2,
  number=226829418, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)


_FILESTATUSANNOTATION = _descriptor.Descriptor(
  name='FileStatusAnnotation',
  full_name='xds.annotations.v3.FileStatusAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='work_in_progress', full_name='xds.annotations.v3.FileStatusAnnotation.work_in_progress', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=89,
  serialized_end=137,
)


_MESSAGESTATUSANNOTATION = _descriptor.Descriptor(
  name='MessageStatusAnnotation',
  full_name='xds.annotations.v3.MessageStatusAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='work_in_progress', full_name='xds.annotations.v3.MessageStatusAnnotation.work_in_progress', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=139,
  serialized_end=190,
)


_FIELDSTATUSANNOTATION = _descriptor.Descriptor(
  name='FieldStatusAnnotation',
  full_name='xds.annotations.v3.FieldStatusAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='work_in_progress', full_name='xds.annotations.v3.FieldStatusAnnotation.work_in_progress', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=192,
  serialized_end=241,
)


_STATUSANNOTATION = _descriptor.Descriptor(
  name='StatusAnnotation',
  full_name='xds.annotations.v3.StatusAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='work_in_progress', full_name='xds.annotations.v3.StatusAnnotation.work_in_progress', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='package_version_status', full_name='xds.annotations.v3.StatusAnnotation.package_version_status', index=1,
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
  serialized_start=243,
  serialized_end=361,
)

_STATUSANNOTATION.fields_by_name['package_version_status'].enum_type = _PACKAGEVERSIONSTATUS
DESCRIPTOR.message_types_by_name['FileStatusAnnotation'] = _FILESTATUSANNOTATION
DESCRIPTOR.message_types_by_name['MessageStatusAnnotation'] = _MESSAGESTATUSANNOTATION
DESCRIPTOR.message_types_by_name['FieldStatusAnnotation'] = _FIELDSTATUSANNOTATION
DESCRIPTOR.message_types_by_name['StatusAnnotation'] = _STATUSANNOTATION
DESCRIPTOR.enum_types_by_name['PackageVersionStatus'] = _PACKAGEVERSIONSTATUS
DESCRIPTOR.extensions_by_name['file_status'] = file_status
DESCRIPTOR.extensions_by_name['message_status'] = message_status
DESCRIPTOR.extensions_by_name['field_status'] = field_status
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FileStatusAnnotation = _reflection.GeneratedProtocolMessageType('FileStatusAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _FILESTATUSANNOTATION,
  '__module__' : 'xds.annotations.v3.status_pb2'
  # @@protoc_insertion_point(class_scope:xds.annotations.v3.FileStatusAnnotation)
  })
_sym_db.RegisterMessage(FileStatusAnnotation)

MessageStatusAnnotation = _reflection.GeneratedProtocolMessageType('MessageStatusAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGESTATUSANNOTATION,
  '__module__' : 'xds.annotations.v3.status_pb2'
  # @@protoc_insertion_point(class_scope:xds.annotations.v3.MessageStatusAnnotation)
  })
_sym_db.RegisterMessage(MessageStatusAnnotation)

FieldStatusAnnotation = _reflection.GeneratedProtocolMessageType('FieldStatusAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _FIELDSTATUSANNOTATION,
  '__module__' : 'xds.annotations.v3.status_pb2'
  # @@protoc_insertion_point(class_scope:xds.annotations.v3.FieldStatusAnnotation)
  })
_sym_db.RegisterMessage(FieldStatusAnnotation)

StatusAnnotation = _reflection.GeneratedProtocolMessageType('StatusAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _STATUSANNOTATION,
  '__module__' : 'xds.annotations.v3.status_pb2'
  # @@protoc_insertion_point(class_scope:xds.annotations.v3.StatusAnnotation)
  })
_sym_db.RegisterMessage(StatusAnnotation)

file_status.message_type = _FILESTATUSANNOTATION
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(file_status)
message_status.message_type = _MESSAGESTATUSANNOTATION
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(message_status)
field_status.message_type = _FIELDSTATUSANNOTATION
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field_status)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)