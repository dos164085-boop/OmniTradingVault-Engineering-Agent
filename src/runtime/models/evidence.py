"""
Evidence domain model.

Represents an immutable engineering fact captured during a Runtime
session.

Evidence contains only observed facts. It never stores conclusions or
engineering decisions.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4


class EvidenceType(str, Enum):
    """
    Supported engineering evidence types.
    """

    ERROR = "ERROR"

    LOG = "LOG"

    COMMAND = "COMMAND"

    OUTPUT = "OUTPUT"

    TEST = "TEST"

    FILE = "FILE"

    COMMIT = "COMMIT"

    NOTE = "NOTE"


@dataclass(slots=True, frozen=True)
class Evidence:
    """
    Immutable engineering evidence.

    Evidence represents a fact observed during an engineering session.
    Facts never change after being recorded.
    """

    type: EvidenceType

    source: str

    content: str

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
        Validate evidence invariants.
        """

        if not self.source.strip():
            raise ValueError(
                "Evidence source cannot be empty."
            )

        if not self.content.strip():
            raise ValueError(
                "Evidence content cannot be empty."
            )
            