"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import github.com.pomerium.pomerium.pkg.grpc.databroker.databroker_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ListDataBrokerRecordsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RECORD_TYPE_FIELD_NUMBER: builtins.int
    record_type: builtins.str
    def __init__(
        self,
        *,
        record_type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["record_type", b"record_type"]) -> None: ...

global___ListDataBrokerRecordsRequest = ListDataBrokerRecordsRequest

class ListDataBrokerRecordsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RECORDS_FIELD_NUMBER: builtins.int
    @property
    def records(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[github.com.pomerium.pomerium.pkg.grpc.databroker.databroker_pb2.Record]: ...
    def __init__(
        self,
        *,
        records: collections.abc.Iterable[github.com.pomerium.pomerium.pkg.grpc.databroker.databroker_pb2.Record] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["records", b"records"]) -> None: ...

global___ListDataBrokerRecordsResponse = ListDataBrokerRecordsResponse

class ListDataBrokerRecordTypesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RECORD_TYPES_FIELD_NUMBER: builtins.int
    @property
    def record_types(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        record_types: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["record_types", b"record_types"]) -> None: ...

global___ListDataBrokerRecordTypesResponse = ListDataBrokerRecordTypesResponse