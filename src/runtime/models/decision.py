"""
Decision domain model.

Represents an engineering decision captured during a Runtime session.

A Decision is the result of engineering reasoning. It is independent
from Evidence and does not persist knowledge.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4


class DecisionStatus(str, Enum):
    """
    Lifecycle states for an engineering decision.
    """

    OPEN = "OPEN"
    VALIDATED = "VALIDATED"
    CLOSED = "CLOSED"


@dataclass(slots=True)
class Decision:
    """
    Represents a technical decision made during an engineering session.
    """

    title: str

    description: str

    rationale: str

    id: UUID = field(default_factory=uuid4)

    status: DecisionStatus = field(
        default=DecisionStatus.OPEN
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def __post_init__(self) -> None:
        """
        Validate decision invariants.
        """

        if not self.title.strip():
            raise ValueError(
                "Decision title cannot be empty."
            )

        if not self.description.strip():
            raise ValueError(
                "Decision description cannot be empty."
            )

        if not self.rationale.strip():
            raise ValueError(
                "Decision rationale cannot be empty."
            )

    def validate(self) -> None:
        """
        Mark the decision as validated.
        """

        if self.status == DecisionStatus.CLOSED:
            raise ValueError(
                "A closed decision cannot be validated."
            )

        self.status = DecisionStatus.VALIDATED
        self._touch()

    def close(self) -> None:
        """
        Close the decision lifecycle.
        """

        self.status = DecisionStatus.CLOSED
        self._touch()

    def is_open(self) -> bool:
        """
        Return True when the decision is still open.
        """

        return self.status == DecisionStatus.OPEN

    def is_validated(self) -> bool:
        """
        Return True when the decision has been validated.
        """

        return self.status == DecisionStatus.VALIDATED

    def _touch(self) -> None:
        """
        Update the modification timestamp.
        """

        self.updated_at = datetime.now(timezone.utc)
        