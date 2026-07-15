"""
Event domain model.

Represents an immutable event captured during a Runtime session.

An Event is the earliest observable fact in the engineering process.
It contains raw information only and never performs interpretation or
knowledge extraction.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4


class EventType(str, Enum):
    """
    Supported Runtime event types.
    """

    USER_INPUT = "USER_INPUT"

    COMMAND_EXECUTED = "COMMAND_EXECUTED"

    COMMAND_OUTPUT = "COMMAND_OUTPUT"

    COMPILER_ERROR = "COMPILER_ERROR"

    TEST_RESULT = "TEST_RESULT"

    GIT_OPERATION = "GIT_OPERATION"

    FILE_CREATED = "FILE_CREATED"

    FILE_UPDATED = "FILE_UPDATED"

    FILE_DELETED = "FILE_DELETED"

    SYSTEM_MESSAGE = "SYSTEM_MESSAGE"

    RUNTIME_EVENT = "RUNTIME_EVENT"

    NOTE = "NOTE"


@dataclass(slots=True, frozen=True)
class Event:
    """
    Immutable Runtime event.

    Events represent observations captured during an engineering
    session. They are immutable and become the input for subsequent
    Runtime components such as Evidence extraction.
    """

    type: EventType

    source: str

    data: str

    id: UUID = field(
        default_factory=uuid4
    )

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(
            timezone.utc
        )
    )

    def __post_init__(self) -> None:
        """
        Validate event invariants.
        """

        if not self.source.strip():
            raise ValueError(
                "Event source cannot be empty."
            )

        if not self.data.strip():
            raise ValueError(
                "Event data cannot be empty."
            )
            