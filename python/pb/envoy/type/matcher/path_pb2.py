# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/type/matcher/path.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.type.matcher import string_pb2 as envoy_dot_type_dot_matcher_dot_string__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/type/matcher/path.proto',
  package='envoy.type.matcher',
  syntax='proto3',
  serialized_options=b'\n io.envoyproxy.envoy.type.matcherB\tPathProtoP\001\272\200\310\321\006\002\020\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1d\x65nvoy/type/matcher/path.proto\x12\x12\x65nvoy.type.matcher\x1a\x1f\x65nvoy/type/matcher/string.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"W\n\x0bPathMatcher\x12;\n\x04path\x18\x01 \x01(\x0b\x32!.envoy.type.matcher.StringMatcherB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00\x42\x0b\n\x04rule\x12\x03\xf8\x42\x01\x42\x37\n io.envoyproxy.envoy.type.matcherB\tPathProtoP\x01\xba\x80\xc8\xd1\x06\x02\x10\x01\x62\x06proto3'
  ,
  dependencies=[envoy_dot_type_dot_matcher_dot_string__pb2.DESCRIPTOR,udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_PATHMATCHER = _descriptor.Descriptor(
  name='PathMatcher',
  full_name='envoy.type.matcher.PathMatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='envoy.type.matcher.PathMatcher.path', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\212\001\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='rule', full_name='envoy.type.matcher.PathMatcher.rule',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=142,
  serialized_end=229,
)

_PATHMATCHER.fields_by_name['path'].message_type = envoy_dot_type_dot_matcher_dot_string__pb2._STRINGMATCHER
_PATHMATCHER.oneofs_by_name['rule'].fields.append(
  _PATHMATCHER.fields_by_name['path'])
_PATHMATCHER.fields_by_name['path'].containing_oneof = _PATHMATCHER.oneofs_by_name['rule']
DESCRIPTOR.message_types_by_name['PathMatcher'] = _PATHMATCHER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PathMatcher = _reflection.GeneratedProtocolMessageType('PathMatcher', (_message.Message,), {
  'DESCRIPTOR' : _PATHMATCHER,
  '__module__' : 'envoy.type.matcher.path_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.matcher.PathMatcher)
  })
_sym_db.RegisterMessage(PathMatcher)


DESCRIPTOR._options = None
_PATHMATCHER.oneofs_by_name['rule']._options = None
_PATHMATCHER.fields_by_name['path']._options = None
# @@protoc_insertion_point(module_scope)