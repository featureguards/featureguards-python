"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import toggles.toggles_pb2
import typing

class TogglesStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Fetch: grpc.UnaryUnaryMultiCallable[
        toggles.toggles_pb2.FetchRequest,
        toggles.toggles_pb2.FetchResponse]

    Listen: grpc.UnaryStreamMultiCallable[
        toggles.toggles_pb2.ListenRequest,
        toggles.toggles_pb2.ListenPayload]


class TogglesServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Fetch(self,
        request: toggles.toggles_pb2.FetchRequest,
        context: grpc.ServicerContext,
    ) -> toggles.toggles_pb2.FetchResponse: ...

    @abc.abstractmethod
    def Listen(self,
        request: toggles.toggles_pb2.ListenRequest,
        context: grpc.ServicerContext,
    ) -> typing.Iterator[toggles.toggles_pb2.ListenPayload]: ...


def add_TogglesServicer_to_server(servicer: TogglesServicer, server: grpc.Server) -> None: ...
