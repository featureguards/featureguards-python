"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class AuthenticateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VERSION_FIELD_NUMBER: builtins.int
    version: typing.Text
    """Mostly for tracking client versions in the wild."""

    def __init__(self,
        *,
        version: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["version",b"version"]) -> None: ...
global___AuthenticateRequest = AuthenticateRequest

class AuthenticateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCESS_TOKEN_FIELD_NUMBER: builtins.int
    REFRESH_TOKEN_FIELD_NUMBER: builtins.int
    access_token: typing.Text
    refresh_token: typing.Text
    def __init__(self,
        *,
        access_token: typing.Text = ...,
        refresh_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["access_token",b"access_token","refresh_token",b"refresh_token"]) -> None: ...
global___AuthenticateResponse = AuthenticateResponse

class RefreshRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REFRESH_TOKEN_FIELD_NUMBER: builtins.int
    refresh_token: typing.Text
    def __init__(self,
        *,
        refresh_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["refresh_token",b"refresh_token"]) -> None: ...
global___RefreshRequest = RefreshRequest

class RefreshResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACCESS_TOKEN_FIELD_NUMBER: builtins.int
    REFRESH_TOKEN_FIELD_NUMBER: builtins.int
    access_token: typing.Text
    refresh_token: typing.Text
    def __init__(self,
        *,
        access_token: typing.Text = ...,
        refresh_token: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["access_token",b"access_token","refresh_token",b"refresh_token"]) -> None: ...
global___RefreshResponse = RefreshResponse