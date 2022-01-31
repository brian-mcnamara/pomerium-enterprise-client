# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/type/v3/semantic_version.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/type/v3/semantic_version.proto',
  package='envoy.type.v3',
  syntax='proto3',
  serialized_options=b'\n\033io.envoyproxy.envoy.type.v3B\024SemanticVersionProtoP\001Z;github.com/envoyproxy/go-control-plane/envoy/type/v3;typev3\272\200\310\321\006\002\020\002',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$envoy/type/v3/semantic_version.proto\x12\renvoy.type.v3\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\"o\n\x0fSemanticVersion\x12\x14\n\x0cmajor_number\x18\x01 \x01(\r\x12\x14\n\x0cminor_number\x18\x02 \x01(\r\x12\r\n\x05patch\x18\x03 \x01(\r:!\x9a\xc5\x88\x1e\x1c\n\x1a\x65nvoy.type.SemanticVersionBz\n\x1bio.envoyproxy.envoy.type.v3B\x14SemanticVersionProtoP\x01Z;github.com/envoyproxy/go-control-plane/envoy/type/v3;typev3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3'
  ,
  dependencies=[udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,udpa_dot_annotations_dot_versioning__pb2.DESCRIPTOR,])




_SEMANTICVERSION = _descriptor.Descriptor(
  name='SemanticVersion',
  full_name='envoy.type.v3.SemanticVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='major_number', full_name='envoy.type.v3.SemanticVersion.major_number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minor_number', full_name='envoy.type.v3.SemanticVersion.minor_number', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='patch', full_name='envoy.type.v3.SemanticVersion.patch', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_options=b'\232\305\210\036\034\n\032envoy.type.SemanticVersion',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=232,
)

DESCRIPTOR.message_types_by_name['SemanticVersion'] = _SEMANTICVERSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SemanticVersion = _reflection.GeneratedProtocolMessageType('SemanticVersion', (_message.Message,), {
  'DESCRIPTOR' : _SEMANTICVERSION,
  '__module__' : 'envoy.type.v3.semantic_version_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.v3.SemanticVersion)
  })
_sym_db.RegisterMessage(SemanticVersion)


DESCRIPTOR._options = None
_SEMANTICVERSION._options = None
# @@protoc_insertion_point(module_scope)
