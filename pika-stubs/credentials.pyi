from typing import Tuple, Type

from . import spec


class PlainCredentials:

    TYPE: str = ...

    username: str = ...
    password: str = ...
    erase_on_connect: bool = ...

    def __init__(self, username: str, password: str, erase_on_connect: bool = ...) -> None: ...

    def response_for(
        self,
        start: spec.Connection.Start,
    ) -> Tuple[str | None, str | None]: ...

    def erase_credentials(self) -> None: ...


class ExternalCredentials:

    TYPE: str = ...

    erase_on_connect: bool = ...

    def response_for(
        self,
        start: spec.Connection.Start,
    ) -> Tuple[str | None, str | None]: ...

    def erase_credentials(self) -> None: ...


_VALID_TYPES = PlainCredentials | ExternalCredentials
VALID_TYPES: list[_VALID_TYPES]
