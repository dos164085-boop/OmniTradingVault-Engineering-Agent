"""
Decision Builder.

Transforms validated engineering Evidence into Decision objects.

This component belongs to the Runtime layer.

It performs no persistence, no learning and no interaction with the
Knowledge Core.
"""

from __future__ import annotations

from src.runtime.models import (
    Decision,
    Evidence,
)


class DecisionBuilder:
    """
    Builds Decision objects from engineering Evidence.

    The builder is deterministic and stateless.
    """

    def build(
        self,
        evidence: Evidence,
    ) -> Decision:
        """
        Build a Decision from immutable Evidence.

        Args:
            evidence:
                Engineering evidence captured by the Runtime.

        Returns:
            A new Decision.
        """

        return Decision(
            title=f"{evidence.type.value}: {evidence.source}",
            description=evidence.content,
            rationale="Automatically generated from engineering evidence.",
        )
    