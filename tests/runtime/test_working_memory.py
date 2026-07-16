"""
Tests for WorkingMemory.
"""

from src.runtime.models import (
    CandidateStatus,
    Decision,
    Event,
    EventType,
    Evidence,
    EvidenceType,
    KnowledgeCandidate,
)

from src.runtime.working_memory import WorkingMemory


def test_memory_starts_empty() -> None:

    memory = WorkingMemory()

    assert memory.event_count == 0
    assert memory.evidence_count == 0
    assert memory.decision_count == 0
    assert memory.candidate_count == 0


def test_add_event() -> None:

    memory = WorkingMemory()

    event = Event(
        type=EventType.COMMAND_EXECUTED,
        source="terminal",
        data="forge test",
    )

    memory.add_event(event)

    assert memory.event_count == 1
    assert memory.events[0] == event


def test_add_evidence() -> None:

    memory = WorkingMemory()

    evidence = Evidence(
        type=EvidenceType.COMMAND,
        source="terminal",
        content="forge test",
    )

    memory.add_evidence(evidence)

    assert memory.evidence_count == 1
    assert memory.evidence[0] == evidence


def test_add_decision() -> None:

    memory = WorkingMemory()

    decision = Decision(
        title="COMMAND: terminal",
        description="forge test",
        rationale="Generated from runtime evidence",
    )

    memory.add_decision(decision)

    assert memory.decision_count == 1
    assert memory.decisions[0] == decision


def test_add_candidate() -> None:

    memory = WorkingMemory()

    decision = Decision(
        title="COMMAND: terminal",
        description="forge test",
        rationale="Generated from runtime evidence",
    )

    candidate = KnowledgeCandidate(
        title=decision.title,
        summary=decision.description,
        decision_ids=[decision.id],
    )

    memory.add_candidate(candidate)

    assert memory.candidate_count == 1
    assert memory.candidates[0] == candidate
    assert candidate.status == CandidateStatus.DRAFT


def test_clear_memory() -> None:

    memory = WorkingMemory()

    event = Event(
        type=EventType.RUNTIME_EVENT,
        source="runtime",
        data="heartbeat",
    )

    memory.add_event(event)

    memory.clear()

    assert memory.event_count == 0
    assert memory.evidence_count == 0
    assert memory.decision_count == 0
    assert memory.candidate_count == 0


def test_multiple_objects() -> None:

    memory = WorkingMemory()

    for i in range(5):

        memory.add_event(
            Event(
                type=EventType.RUNTIME_EVENT,
                source="runtime",
                data=f"event-{i}",
            )
        )

    assert memory.event_count == 5
    