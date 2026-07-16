"""
Runtime Observer.

Transforms Runtime Events into Evidence objects.

The Observer is the first processing stage of the Runtime pipeline.

Event
    ↓
Observer
    ↓
Evidence
"""

from __future__ import annotations

from src.runtime.models import (
    Event,
    Evidence,
    EvidenceType,
)


class Observer:
    """
    Converts Runtime Events into Evidence.

    The Observer performs no inference and no learning.

    Its responsibility is limited to converting
    observed events into verifiable evidence.
    """

    EVENT_TO_EVIDENCE = {
        "COMMAND_EXECUTED": EvidenceType.COMMAND,
        "COMMAND_OUTPUT": EvidenceType.OUTPUT,
        "COMPILER_ERROR": EvidenceType.ERROR,
        "TEST_RESULT": EvidenceType.TEST,
        "GIT_OPERATION": EvidenceType.COMMIT,
        "FILE_CREATED": EvidenceType.FILE,
        "FILE_UPDATED": EvidenceType.FILE,
        "FILE_DELETED": EvidenceType.FILE,
        "USER_INPUT": EvidenceType.NOTE,
        "SYSTEM_MESSAGE": EvidenceType.NOTE,
        "RUNTIME_EVENT": EvidenceType.NOTE,
        "NOTE": EvidenceType.NOTE,
    }

    def observe(
        self,
        event: Event,
    ) -> Evidence:
        """
        Convert an Event into immutable Evidence.
        """

        evidence_type = self.EVENT_TO_EVIDENCE.get(
            event.type.value,
            EvidenceType.NOTE,
        )

        return Evidence(
            type=evidence_type,
            source=event.source,
            content=str(event.data),
        )