"""
Tests for the Runtime Observer.
"""

from src.runtime.models import (
    Event,
    EventType,
    EvidenceType,
)

from src.runtime.observer import Observer


def test_command_executed_event() -> None:

    observer = Observer()

    event = Event(
        type=EventType.COMMAND_EXECUTED,
        source="terminal",
        data="forge test",
    )

    evidence = observer.observe(event)

    assert evidence.type == EvidenceType.COMMAND
    assert evidence.source == "terminal"
    assert evidence.payload == "forge test"


def test_compiler_error_event() -> None:

    observer = Observer()

    event = Event(
        type=EventType.COMPILER_ERROR,
        source="solc",
        data="Stack too deep",
    )

    evidence = observer.observe(event)

    assert evidence.type == EvidenceType.ERROR


def test_test_result_event() -> None:

    observer = Observer()

    event = Event(
        type=EventType.TEST_RESULT,
        source="pytest",
        data="15 passed",
    )

    evidence = observer.observe(event)

    assert evidence.type == EvidenceType.TEST


def test_git_operation_event() -> None:

    observer = Observer()

    event = Event(
        type=EventType.GIT_OPERATION,
        source="git",
        data="commit",
    )

    evidence = observer.observe(event)

    assert evidence.type == EvidenceType.COMMIT


def test_unknown_mapping_defaults_to_note() -> None:
    """
    Defensive test.

    If the mapping changes in the future and an event
    is missing, Observer must never fail.
    """

    observer = Observer()

    observer.EVENT_TO_EVIDENCE.clear()

    event = Event(
        type=EventType.RUNTIME_EVENT,
        source="runtime",
        data="heartbeat",
    )

    evidence = observer.observe(event)

    assert evidence.type == EvidenceType.NOTE
    