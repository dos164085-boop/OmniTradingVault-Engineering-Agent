"""
Runtime Pipeline.

Coordinates the Runtime processing flow.

The RuntimePipeline orchestrates the Runtime components while
maintaining the transient state inside WorkingMemory.

Pipeline

    Event
      │
      ▼
WorkingMemory
      │
      ▼
   Observer
      │
      ▼
   Evidence
      │
      ▼
WorkingMemory
      │
      ▼
DecisionBuilder
      │
      ▼
   Decision
      │
      ▼
WorkingMemory
      │
      ▼
KnowledgeCandidateBuilder
      │
      ▼
KnowledgeCandidate
      │
      ▼
WorkingMemory
      │
      ▼
RuntimeResult
"""

from __future__ import annotations

from src.runtime.decision_builder import DecisionBuilder
from src.runtime.knowledge_candidate_builder import (
    KnowledgeCandidateBuilder,
)
from src.runtime.models import (
    Decision,
    Event,
    Evidence,
    KnowledgeCandidate,
)
from src.runtime.models.runtime_result import (
    RuntimeResult,
)
from src.runtime.observer import Observer
from src.runtime.working_memory import WorkingMemory


class RuntimePipeline:
    """
    Coordinates the Runtime processing pipeline.

    The RuntimePipeline owns no business logic.

    Its responsibility is limited to orchestrating Runtime
    components while maintaining transient execution state.
    """

    def __init__(self) -> None:

        self._observer = Observer()

        self._decision_builder = (
            DecisionBuilder()
        )

        self._candidate_builder = (
            KnowledgeCandidateBuilder()
        )

        self._memory = WorkingMemory()

    @property
    def memory(
        self,
    ) -> WorkingMemory:
        """
        Return the current WorkingMemory.
        """

        return self._memory

    def process(
        self,
        event: Event,
    ) -> RuntimeResult:
        """
        Execute the complete Runtime pipeline.

        Args:
            event:
                Runtime Event.

        Returns:
            RuntimeResult containing every artifact
            produced during execution.
        """

        self._memory.add_event(
            event
        )

        evidence = self.observe(
            event
        )

        decision = self.build_decision(
            evidence
        )

        candidate = self.build_candidate(
            decision
        )

        return RuntimeResult(
            event=event,
            evidence=evidence,
            decision=decision,
            candidate=candidate,
        )

    def observe(
        self,
        event: Event,
    ) -> Evidence:
        """
        Execute Observer stage.
        """

        evidence = self._observer.observe(
            event
        )

        self._memory.add_evidence(
            evidence
        )

        return evidence

    def build_decision(
        self,
        evidence: Evidence,
    ) -> Decision:
        """
        Execute DecisionBuilder stage.
        """

        decision = (
            self._decision_builder.build(
                evidence
            )
        )

        self._memory.add_decision(
            decision
        )

        return decision

    def build_candidate(
        self,
        decision: Decision,
    ) -> KnowledgeCandidate:
        """
        Execute KnowledgeCandidateBuilder stage.
        """

        candidate = (
            self._candidate_builder.build(
                decision
            )
        )

        self._memory.add_candidate(
            candidate
        )

        return candidate

    def clear(
        self,
    ) -> None:
        """
        Reset Runtime state.
        """

        self._memory.clear()