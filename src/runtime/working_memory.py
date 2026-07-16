"""
Working Memory.

Stores the transient engineering state of the Runtime.

WorkingMemory represents the active context of an engineering
session. It is completely in-memory and is discarded when the
Runtime finishes.

Nothing stored here becomes persistent knowledge.
"""

from __future__ import annotations

from src.runtime.models import (
    Decision,
    Event,
    Evidence,
    KnowledgeCandidate,
)


class WorkingMemory:
    """
    In-memory Runtime state.

    The WorkingMemory owns no business logic.

    Its responsibility is to maintain the temporary engineering
    artifacts produced during a Runtime session.
    """

    def __init__(self) -> None:
        self.clear()

    def add_event(
        self,
        event: Event,
    ) -> None:
        """
        Store a Runtime Event.
        """

        self.events.append(event)

    def add_evidence(
        self,
        evidence: Evidence,
    ) -> None:
        """
        Store Evidence.
        """

        self.evidence.append(evidence)

    def add_decision(
        self,
        decision: Decision,
    ) -> None:
        """
        Store a Decision.
        """

        self.decisions.append(decision)

    def add_candidate(
        self,
        candidate: KnowledgeCandidate,
    ) -> None:
        """
        Store a KnowledgeCandidate.
        """

        self.candidates.append(candidate)

    def clear(self) -> None:
        """
        Reset Runtime state.
        """

        self.events: list[Event] = []

        self.evidence: list[Evidence] = []

        self.decisions: list[Decision] = []

        self.candidates: list[
            KnowledgeCandidate
        ] = []

    @property
    def event_count(
        self,
    ) -> int:
        """
        Return the number of Events.
        """

        return len(self.events)

    @property
    def evidence_count(
        self,
    ) -> int:
        """
        Return the number of Evidence items.
        """

        return len(self.evidence)

    @property
    def decision_count(
        self,
    ) -> int:
        """
        Return the number of Decisions.
        """

        return len(self.decisions)

    @property
    def candidate_count(
        self,
    ) -> int:
        """
        Return the number of KnowledgeCandidates.
        """

        return len(self.candidates)