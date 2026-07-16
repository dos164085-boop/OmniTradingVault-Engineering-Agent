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
    assert evidence.content == "forge test"


def test_command_output_event() -> None:

    observer = Observer()

    event = Event(
        type=EventType.COMMAND_OUTPUT,
        source="terminal",
        data="Compilation completed",
    )

    evidence = observer.observe(event)

    assert evidence.type == EvidenceType.OUTPUT
    assert evidence.content == "Compilation completed"


def test_compiler_error_event() -> None:

    observer = Observer()

    event = Event(
        type=EventType.COMPILER_ERROR,
        source="solc",
        data="Stack too deep",
    )

    evidence = observer.observe(event)

    assert evidence.type == EvidenceType.ERROR
    assert evidence.content == "Stack too deep"


def test_test_result_event() -> None:

    observer = Observer()

    event = Event(
        type=EventType.TEST_RESULT,
        source="pytest",
        data="15 passed",
    )

    evidence = observer.observe(event)

    assert evidence.type == EvidenceType.TEST
    assert evidence.content == "15 passed"


def test_git_operation_event() -> None:

    observer = Observer()

    event = Event(
        type=EventType.GIT_OPERATION,
        source="git",
        data="commit",
    )

    evidence = observer.observe(event)

    assert evidence.type == EvidenceType.COMMIT
    assert evidence.content == "commit"


def test_file_created_event() -> None:

    observer = Observer()

    event = Event(
        type=EventType.FILE_CREATED,
        source="filesystem",
        data="src/runtime/observer.py",
    )

    evidence = observer.observe(event)

    assert evidence.type == EvidenceType.FILE
    assert evidence.content == "src/runtime/observer.py"


def test_unknown_mapping_defaults_to_note() -> None:
    """
    Observer must always return valid Evidence even if
    the mapping is incomplete.
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
    assert evidence.content == "heartbeat"  