"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import settings_pb2

class SettingsServiceStub:
    """SettingsService manages global pomerium settings"""

    def __init__(self, channel: grpc.Channel) -> None: ...
    GetSettings: grpc.UnaryUnaryMultiCallable[
        settings_pb2.GetSettingsRequest,
        settings_pb2.GetSettingsResponse,
    ]
    """GetSettings retrieves the currently applied settings"""
    SetSettings: grpc.UnaryUnaryMultiCallable[
        settings_pb2.SetSettingsRequest,
        settings_pb2.SetSettingsResponse,
    ]
    """SetSettings applies new global settings"""

class SettingsServiceServicer(metaclass=abc.ABCMeta):
    """SettingsService manages global pomerium settings"""

    @abc.abstractmethod
    def GetSettings(
        self,
        request: settings_pb2.GetSettingsRequest,
        context: grpc.ServicerContext,
    ) -> settings_pb2.GetSettingsResponse:
        """GetSettings retrieves the currently applied settings"""
    @abc.abstractmethod
    def SetSettings(
        self,
        request: settings_pb2.SetSettingsRequest,
        context: grpc.ServicerContext,
    ) -> settings_pb2.SetSettingsResponse:
        """SetSettings applies new global settings"""

def add_SettingsServiceServicer_to_server(servicer: SettingsServiceServicer, server: grpc.Server) -> None: ...
