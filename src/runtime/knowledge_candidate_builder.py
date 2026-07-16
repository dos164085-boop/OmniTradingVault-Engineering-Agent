"""
Knowledge Candidate Builder.

Builds KnowledgeCandidate objects from validated engineering Decisions.

This component belongs to the Runtime layer.

It performs no persistence, no AI inference and no interaction with the
Knowledge Core.
"""

from __future__ import annotations

from src.runtime.models import (
    Decision,
    KnowledgeCandidate,
)


class KnowledgeCandidateBuilder:
    """
    Builds KnowledgeCandidate objects from validated Decisions.

    The builder is deterministic and stateless. Its responsibility is
    limited to transforming engineering decisions into candidates that
    may later be evaluated by the Knowledge Core.
    """

    def build(
        self,
        decision: Decision,
    ) -> KnowledgeCandidate:
        """
        Build a KnowledgeCandidate from a Decision.

        Args:
            decision:
                Validated engineering decision.

        Returns:
            A new KnowledgeCandidate.
        """

        return KnowledgeCandidate(
            title=decision.title,
            summary=decision.description,
            decision_ids=[decision.id],
        )
    