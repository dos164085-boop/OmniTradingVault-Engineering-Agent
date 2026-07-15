"""
Session domain model.

Represents an active engineering session inside Leo Runtime.

A session is the temporal container where engineering decisions,
evidence and context are collected.

This module belongs to runtime and must not depend on Knowledge Core.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4


class SessionStatus(str, Enum):
    """
    Lifecycle states for an engineering session.
    """

    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"


@dataclass
class Session:
    """
    Represents an engineering work session.

    A Session owns the context of a single engineering activity.
    It does not persist knowledge and does not communicate with
    external systems.

    Attributes:
        id:
            Unique identifier for the session.

        title:
            Human-readable session description.

        status:
            Current lifecycle status.

        created_at:
            Creation timestamp.

        updated_at:
            Last modification timestamp.

        decision_ids:
            Decisions associated with this session.
    """

    title: str

    id: UUID = field(default_factory=uuid4)

    status: SessionStatus = field(
        default=SessionStatus.ACTIVE
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    decision_ids: list[UUID] = field(default_factory=list)

    def __post_init__(self) -> None:
        """
        Validate session invariants.
        """

        if not self.title.strip():
            raise ValueError(
                "Session title cannot be empty"
            )

    def add_decision(self, decision_id: UUID) -> None:
        """
        Associate a decision with this session.

        Args:
            decision_id:
                Identifier of the decision to attach.
        """

        if self.status == SessionStatus.CLOSED:
            raise ValueError(
                "Cannot add decisions to a closed session"
            )

        if decision_id not in self.decision_ids:
            self.decision_ids.append(decision_id)

        self._touch()

    def close(self) -> None:
        """
        Close the engineering session.
        """

        self.status = SessionStatus.CLOSED
        self._touch()

    def is_active(self) -> bool:
        """
        Return whether the session is currently active.
        """

        return self.status == SessionStatus.ACTIVE

    def _touch(self) -> None:
        """
        Update modification timestamp.
        """

        self.updated_at = datetime.now(timezone.utc)
        