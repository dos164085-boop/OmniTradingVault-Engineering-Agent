"""
Tests for the Runtime Pipeline.
"""

from src.runtime.models import (
    CandidateStatus,
    Event,
    EventType,
)

from src.runtime.models.runtime_result import RuntimeResult
from src.runtime.runtime_pipeline import RuntimePipeline


def test_process_command_event() -> None:
    """
    A command event should produce a RuntimeResult.
    """

    pipeline = RuntimePipeline()

    event = Event(
        type=EventType.COMMAND_EXECUTED,
        source="terminal",
        data="forge test",
    )

    result = pipeline.process(event)

    assert isinstance(result, RuntimeResult)

    assert result.candidate.title == "COMMAND: terminal"
    assert result.candidate.summary == "forge test"
    assert result.candidate.status == CandidateStatus.DRAFT

    assert len(result.candidate.decision_ids) == 1


def test_process_compiler_error() -> None:

    pipeline = RuntimePipeline()

    event = Event(
        type=EventType.COMPILER_ERROR,
        source="solc",
        data="Stack too deep",
    )

    result = pipeline.process(event)

    assert result.candidate.title == "ERROR: solc"
    assert result.candidate.summary == "Stack too deep"


def test_process_test_result() -> None:

    pipeline = RuntimePipeline()

    event = Event(
        type=EventType.TEST_RESULT,
        source="pytest",
        data="25 passed",
    )

    result = pipeline.process(event)

    assert result.candidate.title == "TEST: pytest"
    assert result.candidate.summary == "25 passed"


def test_pipeline_is_deterministic() -> None:

    pipeline = RuntimePipeline()

    event = Event(
        type=EventType.FILE_CREATED,
        source="filesystem",
        data="observer.py",
    )

    first = pipeline.process(event)

    second = pipeline.process(event)

    assert first.candidate.title == second.candidate.title
    assert first.candidate.summary == second.candidate.summary

    assert first.decision.title == second.decision.title
    assert first.evidence.content == second.evidence.content


def test_observe_stage() -> None:

    pipeline = RuntimePipeline()

    event = Event(
        type=EventType.RUNTIME_EVENT,
        source="runtime",
        data="heartbeat",
    )

    evidence = pipeline.observe(event)

    assert evidence.source == "runtime"


def test_build_decision_stage() -> None:

    pipeline = RuntimePipeline()

    event = Event(
        type=EventType.COMMAND_EXECUTED,
        source="terminal",
        data="python -m pytest",
    )

    evidence = pipeline.observe(event)

    decision = pipeline.build_decision(evidence)

    assert decision.title == "COMMAND: terminal"
    assert decision.is_open()


def test_build_candidate_stage() -> None:

    pipeline = RuntimePipeline()

    event = Event(
        type=EventType.COMMAND_EXECUTED,
        source="terminal",
        data="forge build",
    )

    evidence = pipeline.observe(event)

    decision = pipeline.build_decision(evidence)

    candidate = pipeline.build_candidate(decision)

    assert candidate.status == CandidateStatus.DRAFT
    assert candidate.decision_ids == [decision.id]