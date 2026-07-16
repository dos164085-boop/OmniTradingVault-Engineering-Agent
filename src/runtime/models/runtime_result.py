"""
Runtime Result domain model.

Represents the complete result of a Runtime execution.

A RuntimeResult groups every artifact produced while processing
a Runtime Event.

It is a transient domain object and is never persisted.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from src.runtime.models.decision import Decision
from src.runtime.models.event import Event
from src.runtime.models.evidence import Evidence
from src.runtime.models.knowledge_candidate import (
    KnowledgeCandidate,
)


@dataclass(slots=True, frozen=True)
class RuntimeResult:
    """
    Complete Runtime execution result.

    Attributes:
        event:
            Original Runtime event.

        evidence:
            Evidence produced by the Observer.

        decision:
            Decision produced by the DecisionBuilder.

        candidate:
            KnowledgeCandidate produced by the
            KnowledgeCandidateBuilder.

        created_at:
            Execution timestamp.
    """

    event: Event

    evidence: Evidence

    decision: Decision

    candidate: KnowledgeCandidate

    created_at: datetime = datetime.now(
        timezone.utc
    )

    def __post_init__(self) -> None:
        """
        Validate RuntimeResult invariants.
        """

        if self.event is None:
            raise ValueError(
                "RuntimeResult requires an Event."
            )

        if self.evidence is None:
            raise ValueError(
                "RuntimeResult requires Evidence."
            )

        if self.decision is None:
            raise ValueError(
                "RuntimeResult requires a Decision."
            )

        if self.candidate is None:
            raise ValueError(
                "RuntimeResult requires a KnowledgeCandidate."
            )