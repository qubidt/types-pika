from __future__ import annotations

from typing import Any, List, Mapping, Optional, Type

from . import amqp_object

PROTOCOL_VERSION: Any
PORT: int

ACCESS_REFUSED: int
CHANNEL_ERROR: int
COMMAND_INVALID: int
CONNECTION_FORCED: int
CONTENT_TOO_LARGE: int
FRAME_BODY: int
FRAME_END: int
FRAME_END_SIZE: int
FRAME_ERROR: int
FRAME_HEADER: int
FRAME_HEADER_SIZE: int
FRAME_HEARTBEAT: int
FRAME_MAX_SIZE: int
FRAME_METHOD: int
FRAME_MIN_SIZE: int
INTERNAL_ERROR: int
INVALID_PATH: int
NOT_ALLOWED: int
NOT_FOUND: int
NOT_IMPLEMENTED: int
NO_CONSUMERS: int
NO_ROUTE: int
PERSISTENT_DELIVERY_MODE: int
PRECONDITION_FAILED: int
REPLY_SUCCESS: int
RESOURCE_ERROR: int
RESOURCE_LOCKED: int
SYNTAX_ERROR: int
TRANSIENT_DELIVERY_MODE: int
UNEXPECTED_FRAME: int


class Connection(amqp_object.Class):

    INDEX: int
    NAME: str

    class Start(amqp_object.Method):

        INDEX: int
        NAME: str

        version_major: int
        version_minor: int
        server_properties: Optional[Mapping[str, Any]]
        mechanisms: str
        locales: str

        def __init__(
            self,
            version_major: int,
            version_minor: int,
            server_properties: Optional[Mapping[str, Any]],
            mechanisms: str,
            locales: str,
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Connection.Start: ...
        def encode(self) -> List[bytes]: ...

    class StartOk(amqp_object.Method):

        INDEX: int
        NAME: str

        client_properties: Optional[Mapping[str, Any]]
        mechanism: str
        response: Optional[str]
        locale: str

        def __init__(
            self,
            client_properties: Optional[Mapping[str, Any]],
            mechanism: str,
            response: Optional[str],
            locale: str,
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Connection.StartOk: ...
        def encode(self) -> List[bytes]: ...

    class Secure(amqp_object.Method):

        INDEX: int
        NAME: str

        challenge: Optional[str]

        def __init__(self, challenge: Optional[str]) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Connection.Secure: ...
        def encode(self) -> List[bytes]: ...

    class SecureOk(amqp_object.Method):

        INDEX: int
        NAME: str

        response: Optional[str]

        def __init__(self, response: Optional[str]) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Connection.SecureOk: ...
        def encode(self) -> List[bytes]: ...

    class Tune(amqp_object.Method):

        INDEX: int
        NAME: str

        channel_max: int
        frame_max: int
        heartbeat: int

        def __init__(self, channel_max: int, frame_max: int, heartbeat: int) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Connection.Tune: ...
        def encode(self) -> List[bytes]: ...

    class TuneOk(amqp_object.Method):

        INDEX: int
        NAME: str

        channel_max: int
        frame_max: int
        heartbeat: int

        def __init__(self, channel_max: int, frame_max: int, heartbeat: int) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Connection.TuneOk: ...
        def encode(self) -> List[bytes]: ...

    class Open(amqp_object.Method):

        INDEX: int
        NAME: str

        virtual_host: str
        capabilities: str
        insist: bool

        def __init__(self, virtual_host: str, capabilities: str, insist: bool) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Connection.Open: ...
        def encode(self) -> List[bytes]: ...

    class OpenOk(amqp_object.Method):

        INDEX: int
        NAME: str

        known_hosts: str

        def __init__(self, known_hosts: str) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Connection.OpenOk: ...
        def encode(self) -> List[bytes]: ...

    class Close(amqp_object.Method):

        INDEX: int
        NAME: str

        reply_code: Optional[int]
        reply_text: str
        class_id: Optional[int]
        method_id: Optional[int]

        def __init__(
            self,
            reply_code: Optional[int],
            reply_text: str,
            class_id: Optional[int],
            method_id: Optional[int],
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Connection.Close: ...
        def encode(self) -> List[bytes]: ...

    class CloseOk(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Connection.CloseOk: ...
        def encode(self) -> List[bytes]: ...

    class Blocked(amqp_object.Method):

        INDEX: int
        NAME: str

        reason: str

        def __init__(self, reason: str) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Connection.Blocked: ...
        def encode(self) -> List[bytes]: ...

    class Unblocked(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Connection.Unblocked: ...
        def encode(self) -> List[bytes]: ...


class Channel(amqp_object.Class):

    INDEX: int
    NAME: str

    class Open(amqp_object.Method):

        INDEX: int
        NAME: str

        out_of_band: str

        def __init__(self, out_of_band: str) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Channel.Open: ...
        def encode(self) -> List[bytes]: ...

    class OpenOk(amqp_object.Method):

        INDEX: int
        NAME: str

        channel_id: str

        def __init__(self, channel_id: str) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Channel.OpenOk: ...
        def encode(self) -> List[bytes]: ...

    class Flow(amqp_object.Method):

        INDEX: int
        NAME: str

        active: Optional[bool]

        def __init__(self, active: Optional[bool]) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Channel.Flow: ...
        def encode(self) -> List[bytes]: ...

    class FlowOk(amqp_object.Method):

        INDEX: int
        NAME: str

        active: Optional[bool]

        def __init__(self, active: Optional[bool]) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Channel.FlowOk: ...
        def encode(self) -> List[bytes]: ...

    class Close(amqp_object.Method):

        INDEX: int
        NAME: str

        reply_code: Optional[int]
        reply_text: str
        class_id: Optional[int]
        method_id: Optional[int]

        def __init__(
            self,
            reply_code: Optional[int],
            reply_text: str,
            class_id: Optional[int],
            method_id: Optional[int],
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Channel.Close: ...
        def encode(self) -> List[bytes]: ...

    class CloseOk(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Channel.CloseOk: ...
        def encode(self) -> List[bytes]: ...


class Access(amqp_object.Class):

    INDEX: int
    NAME: str

    class Request(amqp_object.Method):

        INDEX: int
        NAME: str

        realm: str
        exclusive: bool
        passive: bool
        active: bool
        write: bool
        read: bool

        def __init__(
            self,
            realm: str,
            exclusive: bool,
            passive: bool,
            active: bool,
            write: bool,
            read: bool,
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Access.Request: ...
        def encode(self) -> List[bytes]: ...

    class RequestOk(amqp_object.Method):

        INDEX: int
        NAME: str

        ticket: int

        def __init__(self, ticket: int) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Access.RequestOk: ...
        def encode(self) -> List[bytes]: ...


class Exchange(amqp_object.Class):

    INDEX: int
    NAME: str

    class Declare(amqp_object.Method):

        INDEX: int
        NAME: str

        ticket: int
        exchange: Optional[str]
        type: str
        passive: bool
        durable: bool
        auto_delete: bool
        internal: bool
        nowait: bool
        arguments: Optional[Mapping[str, Any]]

        def __init__(
            self,
            ticket: int,
            exchange: Optional[str],
            type: str,
            passive: bool,
            durable: bool,
            auto_delete: bool,
            internal: bool,
            nowait: bool,
            arguments: Optional[Mapping[str, Any]],
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Exchange.Declare: ...
        def encode(self) -> List[bytes]: ...

    class DeclareOk(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Exchange.DeclareOk: ...
        def encode(self) -> List[bytes]: ...

    class Delete(amqp_object.Method):

        INDEX: int
        NAME: str

        ticket: int
        exchange: Optional[str]
        if_unused: bool
        nowait: bool

        def __init__(
            self,
            ticket: int,
            exchange: Optional[str],
            if_unused: bool,
            nowait: bool,
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Exchange.Delete: ...
        def encode(self) -> List[bytes]: ...

    class DeleteOk(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Exchange.DeleteOk: ...
        def encode(self) -> List[bytes]: ...

    class Bind(amqp_object.Method):

        INDEX: int
        NAME: str

        ticket: int
        destination: Optional[str]
        source: Optional[str]
        routing_key: str
        nowait: bool
        arguments: Optional[Mapping[str, Any]]

        def __init__(
            self,
            ticket: int,
            destination: Optional[str],
            source: Optional[str],
            routing_key: str,
            nowait: bool,
            arguments: Optional[Mapping[str, Any]],
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Exchange.Bind: ...
        def encode(self) -> List[bytes]: ...

    class BindOk(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Exchange.BindOk: ...
        def encode(self) -> List[bytes]: ...

    class Unbind(amqp_object.Method):

        INDEX: int
        NAME: str

        ticket: int
        destination: Optional[str]
        source: Optional[str]
        routing_key: str
        nowait: bool
        arguments: Optional[Mapping[str, Any]]

        def __init__(
            self,
            ticket: int,
            destination: Optional[str],
            source: Optional[str],
            routing_key: str,
            nowait: bool,
            arguments: Optional[Mapping[str, Any]],
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Exchange.Unbind: ...
        def encode(self) -> List[bytes]: ...

    class UnbindOk(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Exchange.UnbindOk: ...
        def encode(self) -> List[bytes]: ...


class Queue(amqp_object.Class):

    INDEX: int
    NAME: str

    class Declare(amqp_object.Method):

        INDEX: int
        NAME: str

        ticket: int
        queue: str
        passive: bool
        durable: bool
        exclusive: bool
        auto_delete: bool
        nowait: bool
        arguments: Optional[Mapping[str, Any]]

        def __init__(
            self,
            ticket: int,
            queue: str,
            passive: bool,
            durable: bool,
            exclusive: bool,
            auto_delete: bool,
            nowait: bool,
            arguments: Optional[Mapping[str, Any]],
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Queue.Declare: ...
        def encode(self) -> List[bytes]: ...

    class DeclareOk(amqp_object.Method):

        INDEX: int
        NAME: str

        queue: Optional[str]
        message_count: Optional[int]
        consumer_count: Optional[int]

        def __init__(
            self,
            queue: Optional[str],
            message_count: Optional[int],
            consumer_count: Optional[int],
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Queue.DeclareOk: ...
        def encode(self) -> List[bytes]: ...

    class Bind(amqp_object.Method):

        INDEX: int
        NAME: str

        ticket: int
        queue: str
        exchange: Optional[str]
        routing_key: str
        nowait: bool
        arguments: Optional[Mapping[str, Any]]

        def __init__(
            self,
            ticket: int,
            queue: str,
            exchange: Optional[str],
            routing_key: str,
            nowait: bool,
            arguments: Optional[Mapping[str, Any]],
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Queue.Bind: ...
        def encode(self) -> List[bytes]: ...

    class BindOk(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Queue.BindOk: ...
        def encode(self) -> List[bytes]: ...

    class Purge(amqp_object.Method):

        INDEX: int
        NAME: str

        ticket: int
        queue: str
        nowait: bool

        def __init__(self, ticket: int, queue: str, nowait: bool) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Queue.Purge: ...
        def encode(self) -> List[bytes]: ...

    class PurgeOk(amqp_object.Method):

        INDEX: int
        NAME: str

        message_count: Optional[int]

        def __init__(self, message_count: Optional[int]) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Queue.PurgeOk: ...
        def encode(self) -> List[bytes]: ...

    class Delete(amqp_object.Method):

        INDEX: int
        NAME: str

        ticket: int
        queue: str
        if_unused: bool
        if_empty: bool
        nowait: bool

        def __init__(
            self,
            ticket: int,
            queue: str,
            if_unused: bool,
            if_empty: bool,
            nowait: bool,
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Queue.Delete: ...
        def encode(self) -> List[bytes]: ...

    class DeleteOk(amqp_object.Method):

        INDEX: int
        NAME: str

        message_count: Optional[int]

        def __init__(self, message_count: Optional[int]) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Queue.DeleteOk: ...
        def encode(self) -> List[bytes]: ...

    class Unbind(amqp_object.Method):

        INDEX: int
        NAME: str

        ticket: int
        queue: str
        exchange: Optional[str]
        routing_key: str
        arguments: Optional[Mapping[str, Any]]

        def __init__(
            self,
            ticket: int,
            queue: str,
            exchange: Optional[str],
            routing_key: str,
            arguments: Optional[Mapping[str, Any]],
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Queue.Unbind: ...
        def encode(self) -> List[bytes]: ...

    class UnbindOk(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Queue.UnbindOk: ...
        def encode(self) -> List[bytes]: ...


class Basic(amqp_object.Class):

    INDEX: int
    NAME: str

    class Qos(amqp_object.Method):

        INDEX: int
        NAME: str

        prefetch_size: int
        prefetch_count: int
        global_qos: bool

        def __init__(self, prefetch_size: int, prefetch_count: int, global_qos: bool) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.Qos: ...
        def encode(self) -> List[bytes]: ...

    class QosOk(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.QosOk: ...
        def encode(self) -> List[bytes]: ...

    class Consume(amqp_object.Method):

        INDEX: int
        NAME: str

        ticket: int
        queue: str
        consumer_tag: str
        no_local: bool
        no_ack: bool
        exclusive: bool
        nowait: bool
        arguments: Optional[Mapping[str, Any]]

        def __init__(
            self,
            ticket: int,
            queue: str,
            consumer_tag: str,
            no_local: bool,
            no_ack: bool,
            exclusive: bool,
            nowait: bool,
            arguments: Optional[Mapping[str, Any]],
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.Consume: ...
        def encode(self) -> List[bytes]: ...

    class ConsumeOk(amqp_object.Method):

        INDEX: int
        NAME: str

        consumer_tag: Optional[int]

        def __init__(self, consumer_tag: Optional[int]) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.ConsumeOk: ...
        def encode(self) -> List[bytes]: ...

    class Cancel(amqp_object.Method):

        INDEX: int
        NAME: str

        consumer_tag: Optional[int]
        nowait: bool

        def __init__(self, consumer_tag: Optional[int], nowait: bool) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.Cancel: ...
        def encode(self) -> List[bytes]: ...

    class CancelOk(amqp_object.Method):

        INDEX: int
        NAME: str

        consumer_tag: Optional[int]

        def __init__(self, consumer_tag: Optional[int]) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.CancelOk: ...
        def encode(self) -> List[bytes]: ...

    class Publish(amqp_object.Method):

        INDEX: int
        NAME: str

        ticket: int
        exchange: str
        routing_key: str
        mandatory: bool
        immediate: bool

        def __init__(
            self,
            ticket: int,
            exchange: str,
            routing_key: str,
            mandatory: bool,
            immediate: bool,
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.Publish: ...
        def encode(self) -> List[bytes]: ...

    class Return(amqp_object.Method):

        INDEX: int
        NAME: str

        reply_code: Optional[int]
        reply_text: str
        exchange: Optional[str]
        routing_key: Optional[str]

        def __init__(
            self,
            reply_code: Optional[int],
            reply_text: str,
            exchange: Optional[str],
            routing_key: Optional[str],
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.Return: ...
        def encode(self) -> List[bytes]: ...

    class Deliver(amqp_object.Method):

        INDEX: int
        NAME: str

        consumer_tag: Optional[str]
        delivery_tag: Optional[int]
        redelivered: bool
        exchange: Optional[str]
        routing_key: Optional[str]

        def __init__(
            self,
            consumer_tag: Optional[str],
            delivery_tag: Optional[int],
            redelivered: bool,
            exchange: Optional[str],
            routing_key: Optional[str],
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.Deliver: ...
        def encode(self) -> List[bytes]: ...

    class Get(amqp_object.Method):

        INDEX: int
        NAME: str

        ticket: int
        queue: str
        no_ack: bool

        def __init__(self, ticket: int, queue: str, no_ack: bool) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.Get: ...
        def encode(self) -> List[bytes]: ...

    class GetOk(amqp_object.Method):

        INDEX: int
        NAME: str

        delivery_tag: Optional[int]
        redelivered: bool
        exchange: Optional[str]
        routing_key: Optional[str]
        message_count: Optional[int]

        def __init__(
            self,
            delivery_tag: Optional[int],
            redelivered: bool,
            exchange: Optional[str],
            routing_key: Optional[str],
            message_count: Optional[int],
        ) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.GetOk: ...
        def encode(self) -> List[bytes]: ...

    class GetEmpty(amqp_object.Method):

        INDEX: int
        NAME: str

        cluster_id: str

        def __init__(self, cluster_id: str) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.GetEmpty: ...
        def encode(self) -> List[bytes]: ...

    class Ack(amqp_object.Method):

        INDEX: int
        NAME: str

        delivery_tag: int
        multiple: bool

        def __init__(self, delivery_tag: int, multiple: bool) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.Ack: ...
        def encode(self) -> List[bytes]: ...

    class Reject(amqp_object.Method):

        INDEX: int
        NAME: str

        delivery_tag: Optional[int]
        requeue: bool

        def __init__(self, delivery_tag: Optional[int], requeue: bool) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.Reject: ...
        def encode(self) -> List[bytes]: ...

    class RecoverAsync(amqp_object.Method):

        INDEX: int
        NAME: str

        requeue: bool

        def __init__(self, requeue: bool) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.RecoverAsync: ...
        def encode(self) -> List[bytes]: ...

    class Recover(amqp_object.Method):

        INDEX: int
        NAME: str

        requeue: bool

        def __init__(self, requeue: bool) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.Recover: ...
        def encode(self) -> List[bytes]: ...

    class RecoverOk(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.RecoverOk: ...
        def encode(self) -> List[bytes]: ...

    class Nack(amqp_object.Method):

        INDEX: int
        NAME: str

        delivery_tag: int
        multiple: bool
        requeue: bool

        def __init__(self, delivery_tag: int, multiple: bool, requeue: bool) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Basic.Nack: ...
        def encode(self) -> List[bytes]: ...


class Tx(amqp_object.Class):

    INDEX: int
    NAME: str

    class Select(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Tx.Select: ...
        def encode(self) -> List[bytes]: ...

    class SelectOk(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Tx.SelectOk: ...
        def encode(self) -> List[bytes]: ...

    class Commit(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Tx.Commit: ...
        def encode(self) -> List[bytes]: ...

    class CommitOk(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Tx.CommitOk: ...
        def encode(self) -> List[bytes]: ...

    class Rollback(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Tx.Rollback: ...
        def encode(self) -> List[bytes]: ...

    class RollbackOk(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Tx.RollbackOk: ...
        def encode(self) -> List[bytes]: ...


class Confirm(amqp_object.Class):

    INDEX: int
    NAME: str

    class Select(amqp_object.Method):

        INDEX: int
        NAME: str

        nowait: bool

        def __init__(self, nowait: bool) -> None: ...

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Confirm.Select: ...
        def encode(self) -> List[bytes]: ...

    class SelectOk(amqp_object.Method):

        INDEX: int
        NAME: str

        @property
        def synchronous(self) -> bool: ...

        def decode(self, encoded: bytes, offset: int) -> Confirm.SelectOk: ...
        def encode(self) -> List[bytes]: ...


class BasicProperties(amqp_object.Properties):

    CLASS: Type[Basic]

    INDEX: int
    NAME: str

    FLAG_CONTENT_TYPE: int
    FLAG_CONTENT_ENCODING: int
    FLAG_HEADERS: int
    FLAG_DELIVERY_MODE: int
    FLAG_PRIORITY: int
    FLAG_CORRELATION_ID: int
    FLAG_REPLY_TO: int
    FLAG_EXPIRATION: int
    FLAG_MESSAGE_ID: int
    FLAG_TIMESTAMP: int
    FLAG_TYPE: int
    FLAG_USER_ID: int
    FLAG_APP_ID: int
    FLAG_CLUSTER_ID: int

    content_type: Optional[str]
    content_encoding: Optional[str]
    headers: Optional[Mapping[str, Any]]
    delivery_mode: Optional[int]
    priority: Optional[int]
    correlation_id: Optional[str]
    reply_to: Optional[str]
    expiration: Optional[str]
    message_id: Optional[str]
    timestamp: Optional[int]
    type: Optional[str]
    user_id: Optional[str]
    app_id: Optional[str]
    cluster_id: Optional[str]

    def __init__(
        self,
        content_type: Optional[str],
        content_encoding: Optional[str],
        headers: Optional[Mapping[str, Any]],
        delivery_mode: Optional[int],
        priority: Optional[int],
        correlation_id: Optional[str],
        reply_to: Optional[str],
        expiration: Optional[str],
        message_id: Optional[str],
        timestamp: Optional[int],
        type: Optional[str],
        user_id: Optional[str],
        app_id: Optional[str],
        cluster_id: Optional[str],
    ) -> None: ...

    def decode(self, encoded: bytes, offset: int) -> BasicProperties: ...
    def encode(self) -> List[bytes]: ...


methods: Mapping[int, amqp_object.Method]
props: Mapping[int, amqp_object.Properties]


def has_content(methodNumber: int) -> bool: ...