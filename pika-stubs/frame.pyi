from typing import Any, Generic, Tuple, TypeVar

from . import amqp_object, spec

_Method = TypeVar('_Method', bound=amqp_object.Method)


class Frame(amqp_object.AMQPObject):

    NAME: str = ...

    frame_type: int = ...
    channel_number: int = ...

    def __init__(self, frame_type: int, channel_number: int) -> None: ...
    def marshal(self) -> bytes: ...


class Method(Frame, Generic[_Method]):

    NAME: str = ...

    method: _Method = ...

    def __init__(self, channel_number: int, method: _Method) -> None: ...
    def marshal(self) -> bytes: ...


class Header(Frame):

    NAME: str = ...

    body_size: Any = ...
    properties: spec.BasicProperties = ...

    def __init__(
        self,
        channel_number: int,
        body_size: int,
        props: spec.BasicProperties,
    ) -> None: ...
    def marshal(self) -> bytes: ...


class Body(Frame):

    NAME: str = ...

    fragment: bytes = ...

    def __init__(self, channel_number: int, fragment: bytes) -> None: ...
    def marshal(self) -> bytes: ...


class Heartbeat(Frame):

    NAME: str = ...

    def __init__(self) -> None: ...
    def marshal(self) -> bytes: ...


class ProtocolHeader(amqp_object.AMQPObject):

    NAME: str = ...

    frame_type: int = ...

    major: int = ...
    minor: int = ...
    revision: int = ...

    def __init__(
        self,
        major: int | None = ...,
        minor: int | None = ...,
        revision: int | None = ...,
    ) -> None: ...
    def marshal(self) -> bytes: ...


def decode_frame(data_in: bytes) -> Tuple[int, Frame | None]: ...
