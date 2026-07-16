"""
Tests for the RuntimeResult domain model.
"""

from pytest import raises

from src.runtime.models import (
    Decision,
    Event,
    EventType,
    Evidence,
    EvidenceType,
    KnowledgeCandidate,
)
from src.runtime.models.runtime_result import RuntimeResult


def _decision() -> Decision:
    return Decision(
        title="COMMAND: terminal",
        description="forge test",
        rationale="Generated from runtime evidence",
    )


def _candidate(decision: Decision) -> KnowledgeCandidate:
    return KnowledgeCandidate(
        title=decision.title,
        summary=decision.description,
        decision_ids=[decision.id],
    )


def _event() -> Event:
    return Event(
        type=EventType.COMMAND_EXECUTED,
        source="terminal",
        data="forge test",
    )


def _evidence() -> Evidence:
    return Evidence(
        type=EvidenceType.COMMAND,
        source="terminal",
        content="forge test",
    )


def test_create_runtime_result() -> None:

    decision = _decision()

    result = RuntimeResult(
        event=_event(),
        evidence=_evidence(),
        decision=decision,
        candidate=_candidate(decision),
    )

    assert result.event.source == "terminal"
    assert result.evidence.source == "terminal"
    assert result.decision.title == "COMMAND: terminal"
    assert result.candidate.title == "COMMAND: terminal"


def test_requires_event() -> None:

    decision = _decision()

    with raises(ValueError):
        RuntimeResult(
            event=None,
            evidence=_evidence(),
            decision=decision,
            candidate=_candidate(decision),
        )


def test_requires_evidence() -> None:

    decision = _decision()

    with raises(ValueError):
        RuntimeResult(
            event=_event(),
            evidence=None,
            decision=decision,
            candidate=_candidate(decision),
        )


def test_requires_decision() -> None:

    with raises(ValueError):
        RuntimeResult(
            event=_event(),
            evidence=_evidence(),
            decision=None,
            candidate=None,
        )


def test_requires_candidate() -> None:

    decision = _decision()

    with raises(ValueError):
        RuntimeResult(
            event=_event(),
            evidence=_evidence(),
            decision=decision,
            candidate=None,
        )


def test_runtime_result_is_immutable() -> None:

    decision = _decision()

    result = RuntimeResult(
        event=_event(),
        evidence=_evidence(),
        decision=decision,
        candidate=_candidate(decision),
    )

    with raises(Exception):
        result.event = _event()


def test_runtime_result_contains_same_objects() -> None:

    event = _event()
    evidence = _evidence()
    decision = _decision()
    candidate = _candidate(decision)

    result = RuntimeResult(
        event=event,
        evidence=evidence,
        decision=decision,
        candidate=candidate,
    )

    assert result.event is event
    assert result.evidence is evidence
    assert result.decision is decision
    assert result.candidate is candidate
    