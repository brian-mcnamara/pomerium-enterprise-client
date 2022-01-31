# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/route/v3/scoped_route.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.route.v3 import route_pb2 as envoy_dot_config_dot_route_dot_v3_dot_route__pb2
from udpa.annotations import migrate_pb2 as udpa_dot_annotations_dot_migrate__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/route/v3/scoped_route.proto',
  package='envoy.config.route.v3',
  syntax='proto3',
  serialized_options=b'\n#io.envoyproxy.envoy.config.route.v3B\020ScopedRouteProtoP\001ZDgithub.com/envoyproxy/go-control-plane/envoy/config/route/v3;routev3\272\200\310\321\006\002\020\002',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(envoy/config/route/v3/scoped_route.proto\x12\x15\x65nvoy.config.route.v3\x1a!envoy/config/route/v3/route.proto\x1a\x1eudpa/annotations/migrate.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xd3\x04\n\x18ScopedRouteConfiguration\x12\x11\n\ton_demand\x18\x04 \x01(\x08\x12\x15\n\x04name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x36\n\x18route_configuration_name\x18\x02 \x01(\tB\x14\xf2\x98\xfe\x8f\x05\x0e\x12\x0croute_config\x12\\\n\x13route_configuration\x18\x05 \x01(\x0b\x32).envoy.config.route.v3.RouteConfigurationB\x14\xf2\x98\xfe\x8f\x05\x0e\x12\x0croute_config\x12J\n\x03key\x18\x03 \x01(\x0b\x32\x33.envoy.config.route.v3.ScopedRouteConfiguration.KeyB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x1a\xfc\x01\n\x03Key\x12Y\n\tfragments\x18\x01 \x03(\x0b\x32<.envoy.config.route.v3.ScopedRouteConfiguration.Key.FragmentB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\x1ah\n\x08\x46ragment\x12\x14\n\nstring_key\x18\x01 \x01(\tH\x00:9\x9a\xc5\x88\x1e\x34\n2envoy.api.v2.ScopedRouteConfiguration.Key.FragmentB\x0b\n\x04type\x12\x03\xf8\x42\x01:0\x9a\xc5\x88\x1e+\n)envoy.api.v2.ScopedRouteConfiguration.Key:,\x9a\xc5\x88\x1e\'\n%envoy.api.v2.ScopedRouteConfigurationB\x87\x01\n#io.envoyproxy.envoy.config.route.v3B\x10ScopedRouteProtoP\x01ZDgithub.com/envoyproxy/go-control-plane/envoy/config/route/v3;routev3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3'
  ,
  dependencies=[envoy_dot_config_dot_route_dot_v3_dot_route__pb2.DESCRIPTOR,udpa_dot_annotations_dot_migrate__pb2.DESCRIPTOR,udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,udpa_dot_annotations_dot_versioning__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_SCOPEDROUTECONFIGURATION_KEY_FRAGMENT = _descriptor.Descriptor(
  name='Fragment',
  full_name='envoy.config.route.v3.ScopedRouteConfiguration.Key.Fragment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='string_key', full_name='envoy.config.route.v3.ScopedRouteConfiguration.Key.Fragment.string_key', index=0,
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
  serialized_options=b'\232\305\210\0364\n2envoy.api.v2.ScopedRouteConfiguration.Key.Fragment',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='envoy.config.route.v3.ScopedRouteConfiguration.Key.Fragment.type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=621,
  serialized_end=725,
)

_SCOPEDROUTECONFIGURATION_KEY = _descriptor.Descriptor(
  name='Key',
  full_name='envoy.config.route.v3.ScopedRouteConfiguration.Key',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fragments', full_name='envoy.config.route.v3.ScopedRouteConfiguration.Key.fragments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\222\001\002\010\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SCOPEDROUTECONFIGURATION_KEY_FRAGMENT, ],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036+\n)envoy.api.v2.ScopedRouteConfiguration.Key',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=523,
  serialized_end=775,
)

_SCOPEDROUTECONFIGURATION = _descriptor.Descriptor(
  name='ScopedRouteConfiguration',
  full_name='envoy.config.route.v3.ScopedRouteConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='on_demand', full_name='envoy.config.route.v3.ScopedRouteConfiguration.on_demand', index=0,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='envoy.config.route.v3.ScopedRouteConfiguration.name', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='route_configuration_name', full_name='envoy.config.route.v3.ScopedRouteConfiguration.route_configuration_name', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\230\376\217\005\016\022\014route_config', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='route_configuration', full_name='envoy.config.route.v3.ScopedRouteConfiguration.route_configuration', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\230\376\217\005\016\022\014route_config', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='envoy.config.route.v3.ScopedRouteConfiguration.key', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\212\001\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SCOPEDROUTECONFIGURATION_KEY, ],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036\'\n%envoy.api.v2.ScopedRouteConfiguration',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=226,
  serialized_end=821,
)

_SCOPEDROUTECONFIGURATION_KEY_FRAGMENT.containing_type = _SCOPEDROUTECONFIGURATION_KEY
_SCOPEDROUTECONFIGURATION_KEY_FRAGMENT.oneofs_by_name['type'].fields.append(
  _SCOPEDROUTECONFIGURATION_KEY_FRAGMENT.fields_by_name['string_key'])
_SCOPEDROUTECONFIGURATION_KEY_FRAGMENT.fields_by_name['string_key'].containing_oneof = _SCOPEDROUTECONFIGURATION_KEY_FRAGMENT.oneofs_by_name['type']
_SCOPEDROUTECONFIGURATION_KEY.fields_by_name['fragments'].message_type = _SCOPEDROUTECONFIGURATION_KEY_FRAGMENT
_SCOPEDROUTECONFIGURATION_KEY.containing_type = _SCOPEDROUTECONFIGURATION
_SCOPEDROUTECONFIGURATION.fields_by_name['route_configuration'].message_type = envoy_dot_config_dot_route_dot_v3_dot_route__pb2._ROUTECONFIGURATION
_SCOPEDROUTECONFIGURATION.fields_by_name['key'].message_type = _SCOPEDROUTECONFIGURATION_KEY
DESCRIPTOR.message_types_by_name['ScopedRouteConfiguration'] = _SCOPEDROUTECONFIGURATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScopedRouteConfiguration = _reflection.GeneratedProtocolMessageType('ScopedRouteConfiguration', (_message.Message,), {

  'Key' : _reflection.GeneratedProtocolMessageType('Key', (_message.Message,), {

    'Fragment' : _reflection.GeneratedProtocolMessageType('Fragment', (_message.Message,), {
      'DESCRIPTOR' : _SCOPEDROUTECONFIGURATION_KEY_FRAGMENT,
      '__module__' : 'envoy.config.route.v3.scoped_route_pb2'
      # @@protoc_insertion_point(class_scope:envoy.config.route.v3.ScopedRouteConfiguration.Key.Fragment)
      })
    ,
    'DESCRIPTOR' : _SCOPEDROUTECONFIGURATION_KEY,
    '__module__' : 'envoy.config.route.v3.scoped_route_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.route.v3.ScopedRouteConfiguration.Key)
    })
  ,
  'DESCRIPTOR' : _SCOPEDROUTECONFIGURATION,
  '__module__' : 'envoy.config.route.v3.scoped_route_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.route.v3.ScopedRouteConfiguration)
  })
_sym_db.RegisterMessage(ScopedRouteConfiguration)
_sym_db.RegisterMessage(ScopedRouteConfiguration.Key)
_sym_db.RegisterMessage(ScopedRouteConfiguration.Key.Fragment)


DESCRIPTOR._options = None
_SCOPEDROUTECONFIGURATION_KEY_FRAGMENT.oneofs_by_name['type']._options = None
_SCOPEDROUTECONFIGURATION_KEY_FRAGMENT._options = None
_SCOPEDROUTECONFIGURATION_KEY.fields_by_name['fragments']._options = None
_SCOPEDROUTECONFIGURATION_KEY._options = None
_SCOPEDROUTECONFIGURATION.fields_by_name['name']._options = None
_SCOPEDROUTECONFIGURATION.fields_by_name['route_configuration_name']._options = None
_SCOPEDROUTECONFIGURATION.fields_by_name['route_configuration']._options = None
_SCOPEDROUTECONFIGURATION.fields_by_name['key']._options = None
_SCOPEDROUTECONFIGURATION._options = None
# @@protoc_insertion_point(module_scope)
