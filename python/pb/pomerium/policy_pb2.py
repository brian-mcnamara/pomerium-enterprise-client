# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: policy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='policy.proto',
  package='pomerium.dashboard',
  syntax='proto3',
  serialized_options=b'Z+github.com/pomerium/pomerium-console/pkg/pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cpolicy.proto\x12\x12pomerium.dashboard\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf5\x04\n\x06Policy\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cnamespace_id\x18\n \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bmodified_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x10 \x01(\t\x12\x15\n\rallowed_users\x18\x06 \x03(\t\x12\x16\n\x0e\x61llowed_groups\x18\x07 \x03(\t\x12\x17\n\x0f\x61llowed_domains\x18\x08 \x03(\t\x12L\n\x12\x61llowed_idp_claims\x18\x0e \x03(\x0b\x32\x30.pomerium.dashboard.Policy.AllowedIdpClaimsEntry\x12\x0c\n\x04rego\x18\t \x03(\t\x12\x0b\n\x03ppl\x18\x0f \x01(\t\x12\x10\n\x08\x65nforced\x18\r \x01(\x08\x12\x36\n\x06routes\x18\x0b \x03(\x0b\x32&.pomerium.dashboard.Policy.RoutesEntry\x12\x16\n\x0enamespace_name\x18\x0c \x01(\t\x1aS\n\x15\x41llowedIdpClaimsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.ListValue:\x02\x38\x01\x1a-\n\x0bRoutesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"!\n\x13\x44\x65letePolicyRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x16\n\x14\x44\x65letePolicyResponse\"\x1e\n\x10GetPolicyRequest\x12\n\n\x02id\x18\x01 \x01(\t\"?\n\x11GetPolicyResponse\x12*\n\x06policy\x18\x01 \x01(\x0b\x32\x1a.pomerium.dashboard.Policy\"\xa8\x01\n\x13ListPoliciesRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x12\n\x05query\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x13\n\x06offset\x18\x03 \x01(\x03H\x01\x88\x01\x01\x12\x12\n\x05limit\x18\x04 \x01(\x03H\x02\x88\x01\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tH\x03\x88\x01\x01\x42\x08\n\x06_queryB\t\n\x07_offsetB\x08\n\x06_limitB\x0b\n\t_order_by\"Y\n\x14ListPoliciesResponse\x12,\n\x08policies\x18\x01 \x03(\x0b\x32\x1a.pomerium.dashboard.Policy\x12\x13\n\x0btotal_count\x18\x02 \x01(\x03\">\n\x10SetPolicyRequest\x12*\n\x06policy\x18\x01 \x01(\x0b\x32\x1a.pomerium.dashboard.Policy\"?\n\x11SetPolicyResponse\x12*\n\x06policy\x18\x01 \x01(\x0b\x32\x1a.pomerium.dashboard.Policy2\x89\x03\n\rPolicyService\x12\x61\n\x0c\x44\x65letePolicy\x12\'.pomerium.dashboard.DeletePolicyRequest\x1a(.pomerium.dashboard.DeletePolicyResponse\x12X\n\tGetPolicy\x12$.pomerium.dashboard.GetPolicyRequest\x1a%.pomerium.dashboard.GetPolicyResponse\x12\x61\n\x0cListPolicies\x12\'.pomerium.dashboard.ListPoliciesRequest\x1a(.pomerium.dashboard.ListPoliciesResponse\x12X\n\tSetPolicy\x12$.pomerium.dashboard.SetPolicyRequest\x1a%.pomerium.dashboard.SetPolicyResponseB-Z+github.com/pomerium/pomerium-console/pkg/pbb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_POLICY_ALLOWEDIDPCLAIMSENTRY = _descriptor.Descriptor(
  name='AllowedIdpClaimsEntry',
  full_name='pomerium.dashboard.Policy.AllowedIdpClaimsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pomerium.dashboard.Policy.AllowedIdpClaimsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='pomerium.dashboard.Policy.AllowedIdpClaimsEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=599,
  serialized_end=682,
)

_POLICY_ROUTESENTRY = _descriptor.Descriptor(
  name='RoutesEntry',
  full_name='pomerium.dashboard.Policy.RoutesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pomerium.dashboard.Policy.RoutesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='pomerium.dashboard.Policy.RoutesEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=684,
  serialized_end=729,
)

_POLICY = _descriptor.Descriptor(
  name='Policy',
  full_name='pomerium.dashboard.Policy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pomerium.dashboard.Policy.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='namespace_id', full_name='pomerium.dashboard.Policy.namespace_id', index=1,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='pomerium.dashboard.Policy.created_at', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='modified_at', full_name='pomerium.dashboard.Policy.modified_at', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='deleted_at', full_name='pomerium.dashboard.Policy.deleted_at', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='pomerium.dashboard.Policy.name', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='pomerium.dashboard.Policy.description', index=6,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allowed_users', full_name='pomerium.dashboard.Policy.allowed_users', index=7,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allowed_groups', full_name='pomerium.dashboard.Policy.allowed_groups', index=8,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allowed_domains', full_name='pomerium.dashboard.Policy.allowed_domains', index=9,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allowed_idp_claims', full_name='pomerium.dashboard.Policy.allowed_idp_claims', index=10,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rego', full_name='pomerium.dashboard.Policy.rego', index=11,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ppl', full_name='pomerium.dashboard.Policy.ppl', index=12,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enforced', full_name='pomerium.dashboard.Policy.enforced', index=13,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='routes', full_name='pomerium.dashboard.Policy.routes', index=14,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='namespace_name', full_name='pomerium.dashboard.Policy.namespace_name', index=15,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_POLICY_ALLOWEDIDPCLAIMSENTRY, _POLICY_ROUTESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=729,
)


_DELETEPOLICYREQUEST = _descriptor.Descriptor(
  name='DeletePolicyRequest',
  full_name='pomerium.dashboard.DeletePolicyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pomerium.dashboard.DeletePolicyRequest.id', index=0,
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
  serialized_start=731,
  serialized_end=764,
)


_DELETEPOLICYRESPONSE = _descriptor.Descriptor(
  name='DeletePolicyResponse',
  full_name='pomerium.dashboard.DeletePolicyResponse',
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
  serialized_start=766,
  serialized_end=788,
)


_GETPOLICYREQUEST = _descriptor.Descriptor(
  name='GetPolicyRequest',
  full_name='pomerium.dashboard.GetPolicyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pomerium.dashboard.GetPolicyRequest.id', index=0,
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
  serialized_start=790,
  serialized_end=820,
)


_GETPOLICYRESPONSE = _descriptor.Descriptor(
  name='GetPolicyResponse',
  full_name='pomerium.dashboard.GetPolicyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='policy', full_name='pomerium.dashboard.GetPolicyResponse.policy', index=0,
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
  serialized_start=822,
  serialized_end=885,
)


_LISTPOLICIESREQUEST = _descriptor.Descriptor(
  name='ListPoliciesRequest',
  full_name='pomerium.dashboard.ListPoliciesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='pomerium.dashboard.ListPoliciesRequest.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='query', full_name='pomerium.dashboard.ListPoliciesRequest.query', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='pomerium.dashboard.ListPoliciesRequest.offset', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='pomerium.dashboard.ListPoliciesRequest.limit', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_by', full_name='pomerium.dashboard.ListPoliciesRequest.order_by', index=4,
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
    _descriptor.OneofDescriptor(
      name='_query', full_name='pomerium.dashboard.ListPoliciesRequest._query',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_offset', full_name='pomerium.dashboard.ListPoliciesRequest._offset',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_limit', full_name='pomerium.dashboard.ListPoliciesRequest._limit',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_order_by', full_name='pomerium.dashboard.ListPoliciesRequest._order_by',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=888,
  serialized_end=1056,
)


_LISTPOLICIESRESPONSE = _descriptor.Descriptor(
  name='ListPoliciesResponse',
  full_name='pomerium.dashboard.ListPoliciesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='policies', full_name='pomerium.dashboard.ListPoliciesResponse.policies', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_count', full_name='pomerium.dashboard.ListPoliciesResponse.total_count', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=1058,
  serialized_end=1147,
)


_SETPOLICYREQUEST = _descriptor.Descriptor(
  name='SetPolicyRequest',
  full_name='pomerium.dashboard.SetPolicyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='policy', full_name='pomerium.dashboard.SetPolicyRequest.policy', index=0,
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
  serialized_start=1149,
  serialized_end=1211,
)


_SETPOLICYRESPONSE = _descriptor.Descriptor(
  name='SetPolicyResponse',
  full_name='pomerium.dashboard.SetPolicyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='policy', full_name='pomerium.dashboard.SetPolicyResponse.policy', index=0,
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
  serialized_start=1213,
  serialized_end=1276,
)

_POLICY_ALLOWEDIDPCLAIMSENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_POLICY_ALLOWEDIDPCLAIMSENTRY.containing_type = _POLICY
_POLICY_ROUTESENTRY.containing_type = _POLICY
_POLICY.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_POLICY.fields_by_name['modified_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_POLICY.fields_by_name['deleted_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_POLICY.fields_by_name['allowed_idp_claims'].message_type = _POLICY_ALLOWEDIDPCLAIMSENTRY
_POLICY.fields_by_name['routes'].message_type = _POLICY_ROUTESENTRY
_GETPOLICYRESPONSE.fields_by_name['policy'].message_type = _POLICY
_LISTPOLICIESREQUEST.oneofs_by_name['_query'].fields.append(
  _LISTPOLICIESREQUEST.fields_by_name['query'])
_LISTPOLICIESREQUEST.fields_by_name['query'].containing_oneof = _LISTPOLICIESREQUEST.oneofs_by_name['_query']
_LISTPOLICIESREQUEST.oneofs_by_name['_offset'].fields.append(
  _LISTPOLICIESREQUEST.fields_by_name['offset'])
_LISTPOLICIESREQUEST.fields_by_name['offset'].containing_oneof = _LISTPOLICIESREQUEST.oneofs_by_name['_offset']
_LISTPOLICIESREQUEST.oneofs_by_name['_limit'].fields.append(
  _LISTPOLICIESREQUEST.fields_by_name['limit'])
_LISTPOLICIESREQUEST.fields_by_name['limit'].containing_oneof = _LISTPOLICIESREQUEST.oneofs_by_name['_limit']
_LISTPOLICIESREQUEST.oneofs_by_name['_order_by'].fields.append(
  _LISTPOLICIESREQUEST.fields_by_name['order_by'])
_LISTPOLICIESREQUEST.fields_by_name['order_by'].containing_oneof = _LISTPOLICIESREQUEST.oneofs_by_name['_order_by']
_LISTPOLICIESRESPONSE.fields_by_name['policies'].message_type = _POLICY
_SETPOLICYREQUEST.fields_by_name['policy'].message_type = _POLICY
_SETPOLICYRESPONSE.fields_by_name['policy'].message_type = _POLICY
DESCRIPTOR.message_types_by_name['Policy'] = _POLICY
DESCRIPTOR.message_types_by_name['DeletePolicyRequest'] = _DELETEPOLICYREQUEST
DESCRIPTOR.message_types_by_name['DeletePolicyResponse'] = _DELETEPOLICYRESPONSE
DESCRIPTOR.message_types_by_name['GetPolicyRequest'] = _GETPOLICYREQUEST
DESCRIPTOR.message_types_by_name['GetPolicyResponse'] = _GETPOLICYRESPONSE
DESCRIPTOR.message_types_by_name['ListPoliciesRequest'] = _LISTPOLICIESREQUEST
DESCRIPTOR.message_types_by_name['ListPoliciesResponse'] = _LISTPOLICIESRESPONSE
DESCRIPTOR.message_types_by_name['SetPolicyRequest'] = _SETPOLICYREQUEST
DESCRIPTOR.message_types_by_name['SetPolicyResponse'] = _SETPOLICYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Policy = _reflection.GeneratedProtocolMessageType('Policy', (_message.Message,), {

  'AllowedIdpClaimsEntry' : _reflection.GeneratedProtocolMessageType('AllowedIdpClaimsEntry', (_message.Message,), {
    'DESCRIPTOR' : _POLICY_ALLOWEDIDPCLAIMSENTRY,
    '__module__' : 'policy_pb2'
    # @@protoc_insertion_point(class_scope:pomerium.dashboard.Policy.AllowedIdpClaimsEntry)
    })
  ,

  'RoutesEntry' : _reflection.GeneratedProtocolMessageType('RoutesEntry', (_message.Message,), {
    'DESCRIPTOR' : _POLICY_ROUTESENTRY,
    '__module__' : 'policy_pb2'
    # @@protoc_insertion_point(class_scope:pomerium.dashboard.Policy.RoutesEntry)
    })
  ,
  'DESCRIPTOR' : _POLICY,
  '__module__' : 'policy_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.Policy)
  })
_sym_db.RegisterMessage(Policy)
_sym_db.RegisterMessage(Policy.AllowedIdpClaimsEntry)
_sym_db.RegisterMessage(Policy.RoutesEntry)

DeletePolicyRequest = _reflection.GeneratedProtocolMessageType('DeletePolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPOLICYREQUEST,
  '__module__' : 'policy_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.DeletePolicyRequest)
  })
_sym_db.RegisterMessage(DeletePolicyRequest)

DeletePolicyResponse = _reflection.GeneratedProtocolMessageType('DeletePolicyResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEPOLICYRESPONSE,
  '__module__' : 'policy_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.DeletePolicyResponse)
  })
_sym_db.RegisterMessage(DeletePolicyResponse)

GetPolicyRequest = _reflection.GeneratedProtocolMessageType('GetPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPOLICYREQUEST,
  '__module__' : 'policy_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.GetPolicyRequest)
  })
_sym_db.RegisterMessage(GetPolicyRequest)

GetPolicyResponse = _reflection.GeneratedProtocolMessageType('GetPolicyResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPOLICYRESPONSE,
  '__module__' : 'policy_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.GetPolicyResponse)
  })
_sym_db.RegisterMessage(GetPolicyResponse)

ListPoliciesRequest = _reflection.GeneratedProtocolMessageType('ListPoliciesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPOLICIESREQUEST,
  '__module__' : 'policy_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.ListPoliciesRequest)
  })
_sym_db.RegisterMessage(ListPoliciesRequest)

ListPoliciesResponse = _reflection.GeneratedProtocolMessageType('ListPoliciesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTPOLICIESRESPONSE,
  '__module__' : 'policy_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.ListPoliciesResponse)
  })
_sym_db.RegisterMessage(ListPoliciesResponse)

SetPolicyRequest = _reflection.GeneratedProtocolMessageType('SetPolicyRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETPOLICYREQUEST,
  '__module__' : 'policy_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.SetPolicyRequest)
  })
_sym_db.RegisterMessage(SetPolicyRequest)

SetPolicyResponse = _reflection.GeneratedProtocolMessageType('SetPolicyResponse', (_message.Message,), {
  'DESCRIPTOR' : _SETPOLICYRESPONSE,
  '__module__' : 'policy_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.SetPolicyResponse)
  })
_sym_db.RegisterMessage(SetPolicyResponse)


DESCRIPTOR._options = None
_POLICY_ALLOWEDIDPCLAIMSENTRY._options = None
_POLICY_ROUTESENTRY._options = None

_POLICYSERVICE = _descriptor.ServiceDescriptor(
  name='PolicyService',
  full_name='pomerium.dashboard.PolicyService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1279,
  serialized_end=1672,
  methods=[
  _descriptor.MethodDescriptor(
    name='DeletePolicy',
    full_name='pomerium.dashboard.PolicyService.DeletePolicy',
    index=0,
    containing_service=None,
    input_type=_DELETEPOLICYREQUEST,
    output_type=_DELETEPOLICYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetPolicy',
    full_name='pomerium.dashboard.PolicyService.GetPolicy',
    index=1,
    containing_service=None,
    input_type=_GETPOLICYREQUEST,
    output_type=_GETPOLICYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListPolicies',
    full_name='pomerium.dashboard.PolicyService.ListPolicies',
    index=2,
    containing_service=None,
    input_type=_LISTPOLICIESREQUEST,
    output_type=_LISTPOLICIESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetPolicy',
    full_name='pomerium.dashboard.PolicyService.SetPolicy',
    index=3,
    containing_service=None,
    input_type=_SETPOLICYREQUEST,
    output_type=_SETPOLICYRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_POLICYSERVICE)

DESCRIPTOR.services_by_name['PolicyService'] = _POLICYSERVICE

# @@protoc_insertion_point(module_scope)