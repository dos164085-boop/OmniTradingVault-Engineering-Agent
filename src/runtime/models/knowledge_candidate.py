"""
Knowledge Candidate domain model.

Represents structured engineering knowledge produced from one or more
validated decisions during a Runtime session.

A KnowledgeCandidate is not persistent knowledge. It is an intermediate
artifact that will be evaluated by KnowledgeService before becoming part
of the Knowledge Core.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4


class CandidateStatus(str, Enum):
    """
    Lifecycle states of a Knowledge Candidate.
    """

    DRAFT = "DRAFT"
    READY = "READY"
    PUBLISHED = "PUBLISHED"
    REJECTED = "REJECTED"


@dataclass(slots=True)
class KnowledgeCandidate:
    """
    Represents structured engineering knowledge waiting to be published.

    Attributes:
        id:
            Unique candidate identifier.

        title:
            Human-readable title.

        summary:
            Short engineering summary.

        decision_ids:
            Decisions supporting this candidate.

        status:
            Candidate lifecycle.

        created_at:
            Creation timestamp.

        updated_at:
            Last modification timestamp.
    """

    title: str

    summary: str

    decision_ids: list[UUID]

    id: UUID = field(default_factory=uuid4)

    status: CandidateStatus = field(
        default=CandidateStatus.DRAFT
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def __post_init__(self) -> None:
        """
        Validate candidate invariants.
        """

        if not self.title.strip():
            raise ValueError(
                "Candidate title cannot be empty."
            )

        if not self.summary.strip():
            raise ValueError(
                "Candidate summary cannot be empty."
            )

        if not self.decision_ids:
            raise ValueError(
                "A KnowledgeCandidate requires at least one decision."
            )

    def mark_ready(self) -> None:
        """
        Mark the candidate as ready for publication.
        """

        self.status = CandidateStatus.READY
        self._touch()

    def publish(self) -> None:
        """
        Mark the candidate as published.
        """

        if self.status != CandidateStatus.READY:
            raise ValueError(
                "Candidate must be READY before publication."
            )

        self.status = CandidateStatus.PUBLISHED
        self._touch()

    def reject(self) -> None:
        """
        Reject the candidate.
        """

        self.status = CandidateStatus.REJECTED
        self._touch()

    def is_publishable(self) -> bool:
        """
        Return whether the candidate can be published.
        """

        return self.status == CandidateStatus.READY

    def _touch(self) -> None:
        """
        Update modification timestamp.
        """

        self.updated_at = datetime.now(timezone.utc)
        