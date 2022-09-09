# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: key_chain.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.protobuf.timestamp_pb2
import key_chain_pb2


class KeyChainServiceBase(abc.ABC):

    @abc.abstractmethod
    async def DeleteKeyPair(self, stream: 'grpclib.server.Stream[key_chain_pb2.DeleteKeyPairRequest, key_chain_pb2.DeleteKeyPairResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetKeyPair(self, stream: 'grpclib.server.Stream[key_chain_pb2.GetKeyPairRequest, key_chain_pb2.GetKeyPairResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListKeyPairs(self, stream: 'grpclib.server.Stream[key_chain_pb2.ListKeyPairsRequest, key_chain_pb2.ListKeyPairsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateKeyPair(self, stream: 'grpclib.server.Stream[key_chain_pb2.CreateKeyPairRequest, key_chain_pb2.CreateKeyPairResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateKeyPair(self, stream: 'grpclib.server.Stream[key_chain_pb2.UpdateKeyPairRequest, key_chain_pb2.UpdateKeyPairResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/pomerium.dashboard.KeyChainService/DeleteKeyPair': grpclib.const.Handler(
                self.DeleteKeyPair,
                grpclib.const.Cardinality.UNARY_UNARY,
                key_chain_pb2.DeleteKeyPairRequest,
                key_chain_pb2.DeleteKeyPairResponse,
            ),
            '/pomerium.dashboard.KeyChainService/GetKeyPair': grpclib.const.Handler(
                self.GetKeyPair,
                grpclib.const.Cardinality.UNARY_UNARY,
                key_chain_pb2.GetKeyPairRequest,
                key_chain_pb2.GetKeyPairResponse,
            ),
            '/pomerium.dashboard.KeyChainService/ListKeyPairs': grpclib.const.Handler(
                self.ListKeyPairs,
                grpclib.const.Cardinality.UNARY_UNARY,
                key_chain_pb2.ListKeyPairsRequest,
                key_chain_pb2.ListKeyPairsResponse,
            ),
            '/pomerium.dashboard.KeyChainService/CreateKeyPair': grpclib.const.Handler(
                self.CreateKeyPair,
                grpclib.const.Cardinality.UNARY_UNARY,
                key_chain_pb2.CreateKeyPairRequest,
                key_chain_pb2.CreateKeyPairResponse,
            ),
            '/pomerium.dashboard.KeyChainService/UpdateKeyPair': grpclib.const.Handler(
                self.UpdateKeyPair,
                grpclib.const.Cardinality.UNARY_UNARY,
                key_chain_pb2.UpdateKeyPairRequest,
                key_chain_pb2.UpdateKeyPairResponse,
            ),
        }


class KeyChainServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.DeleteKeyPair = grpclib.client.UnaryUnaryMethod(
            channel,
            '/pomerium.dashboard.KeyChainService/DeleteKeyPair',
            key_chain_pb2.DeleteKeyPairRequest,
            key_chain_pb2.DeleteKeyPairResponse,
        )
        self.GetKeyPair = grpclib.client.UnaryUnaryMethod(
            channel,
            '/pomerium.dashboard.KeyChainService/GetKeyPair',
            key_chain_pb2.GetKeyPairRequest,
            key_chain_pb2.GetKeyPairResponse,
        )
        self.ListKeyPairs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/pomerium.dashboard.KeyChainService/ListKeyPairs',
            key_chain_pb2.ListKeyPairsRequest,
            key_chain_pb2.ListKeyPairsResponse,
        )
        self.CreateKeyPair = grpclib.client.UnaryUnaryMethod(
            channel,
            '/pomerium.dashboard.KeyChainService/CreateKeyPair',
            key_chain_pb2.CreateKeyPairRequest,
            key_chain_pb2.CreateKeyPairResponse,
        )
        self.UpdateKeyPair = grpclib.client.UnaryUnaryMethod(
            channel,
            '/pomerium.dashboard.KeyChainService/UpdateKeyPair',
            key_chain_pb2.UpdateKeyPairRequest,
            key_chain_pb2.UpdateKeyPairResponse,
        )