from __future__ import annotations

import abc
import ssl
from socket import AddressFamily
from socket import SocketKind
from socket import socket
from typing import IO
from typing import Any
from typing import AnyStr
from typing import Callable
from typing import Text

from ... import compat

class AbstractIOServices(compat.AbstractBase):
    @abc.abstractmethod
    def get_native_ioloop(self) -> object: ...
    @abc.abstractmethod
    def close(self) -> None: ...
    @abc.abstractmethod
    def run(self) -> None: ...
    @abc.abstractmethod
    def stop(self) -> None: ...
    @abc.abstractmethod
    def add_callback_threadsafe(self, callback: Callable[[], None]) -> None: ...
    @abc.abstractmethod
    def call_later(self, delay: float, callback: Callable[[], None]) -> AbstractTimerReference: ...
    @abc.abstractmethod
    def getaddrinfo(
        self,
        host: bytearray | bytes | Text | None,
        port: str | int | None,
        on_done: Callable[[BaseException | list[tuple[AddressFamily, SocketKind, int, str, tuple[Any, ...]]]], None],
        family: int = ...,
        socktype: int = ...,
        proto: int = ...,
        flags: int = ...,
    ) -> AbstractIOReference: ...
    @abc.abstractmethod
    def connect_socket(
        self, sock: socket, resolved_addr: Any, on_done: Callable[[BaseException | None], None]
    ) -> AbstractIOReference: ...
    @abc.abstractmethod
    def create_streaming_connection(
        self,
        protocol_factory: Callable[[], AbstractStreamProtocol],
        sock: socket,
        on_done: Callable[[BaseException | tuple[AbstractStreamTransport, AbstractStreamProtocol]], None],
        ssl_context: ssl.SSLContext | None = ...,
        server_hostname: str | None = ...,
    ) -> AbstractIOReference: ...

class AbstractFileDescriptorServices(compat.AbstractBase):
    @abc.abstractmethod
    def set_reader(self, fd: IO[AnyStr], on_readable: Callable[[], None]) -> None: ...
    @abc.abstractmethod
    def remove_reader(self, fd: IO[AnyStr]) -> bool: ...
    @abc.abstractmethod
    def set_writer(self, fd: IO[AnyStr], on_writable: Callable[[], None]) -> None: ...
    @abc.abstractmethod
    def remove_writer(self, fd: IO[AnyStr]) -> bool: ...

class AbstractTimerReference(compat.AbstractBase):
    @abc.abstractmethod
    def cancel(self) -> None: ...

class AbstractIOReference(compat.AbstractBase):
    @abc.abstractmethod
    def cancel(self) -> bool: ...

class AbstractStreamProtocol(compat.AbstractBase):
    @abc.abstractmethod
    def connection_made(self, transport: AbstractStreamTransport) -> None: ...
    @abc.abstractmethod
    def connection_lost(self, error: BaseException | None) -> None: ...
    @abc.abstractmethod
    def eof_received(self) -> Any: ...
    @abc.abstractmethod
    def data_received(self, data: bytes) -> None: ...

class AbstractStreamTransport(compat.AbstractBase):
    @abc.abstractmethod
    def abort(self) -> None: ...
    @abc.abstractmethod
    def get_protocol(self) -> AbstractStreamProtocol: ...
    @abc.abstractmethod
    def write(self, data: bytes) -> None: ...
    @abc.abstractmethod
    def get_write_buffer_size(self) -> int: ...
