from typing import Any, Callable, Mapping, Tuple

from . import amqp_object

_Prefix = int | str
_Key = Any
_Caller = object
_Callback = Callable[..., Any]


def name_or_value(value: amqp_object.AMQPObject) -> str: ...
def sanitize_prefix(function: _Callback) -> _Callback: ...
def check_for_prefix_and_key(function: _Callback) -> _Callback: ...


class CallbackManager:

    CALLS: str = ...
    ARGUMENTS: str = ...
    DUPLICATE_WARNING: str = ...
    CALLBACK: str = ...
    ONE_SHOT: str = ...
    ONLY_CALLER: str = ...

    def add(
        self,
        prefix: _Prefix,
        key: _Key,
        callback: _Callback,
        one_shot: bool = ...,
        only_caller: _Caller | None = ...,
        arguments: Mapping[str, Any] | None = ...,
    ) -> Tuple[_Prefix, Any]: ...

    def clear(self) -> None: ...
    def cleanup(self, prefix: _Prefix) -> bool: ...

    def pending(self, prefix: _Prefix, key: _Key) -> int | None: ...

    def process(
        self,
        prefix: _Prefix,
        key: _Key,
        caller: _Caller,
        *args: Any,
        **keywords: Any,
    ) -> bool: ...

    def remove(
        self,
        prefix: _Prefix,
        key: _Key,
        callback_value: _Callback | None = ...,
        arguments: Mapping[str, Any] | None = ...,
    ) -> bool: ...
    def remove_all(self, prefix: _Prefix, key: _Key) -> None: ...
