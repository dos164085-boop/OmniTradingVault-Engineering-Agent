"""
Tests for the RuntimeEngine.
"""

from __future__ import annotations

import pytest

from src.runtime.models import (
    Event,
    EventType,
    RuntimeResult,
)
from src.runtime.runtime_engine import RuntimeEngine


def create_engine() -> RuntimeEngine:
    """
    Build a RuntimeEngine for testing.
    """

    return RuntimeEngine()


def test_start_session() -> None:

    engine = create_engine()

    session = engine.start(
        "Engineering Session"
    )

    assert session.title == "Engineering Session"

    assert engine.active_session() is session


def test_execute_runtime_event() -> None:

    engine = create_engine()

    engine.start(
        "Runtime"
    )

    event = Event(
        type=EventType.RUNTIME_EVENT,
        source="runtime",
        data="heartbeat",
    )

    result = engine.execute(
        event
    )

    assert isinstance(
        result,
        RuntimeResult,
    )

    assert result.event == event


def test_execute_without_session_should_fail() -> None:

    engine = create_engine()

    event = Event(
        type=EventType.RUNTIME_EVENT,
        source="runtime",
        data="heartbeat",
    )

    with pytest.raises(
        RuntimeError
    ):

        engine.execute(
            event
        )


def test_stop_session() -> None:

    engine = create_engine()

    engine.start(
        "Runtime"
    )

    session = engine.stop()

    assert session.is_active() is False

    assert engine.active_session() is None


def test_stop_without_session_should_fail() -> None:

    engine = create_engine()

    with pytest.raises(
        RuntimeError
    ):

        engine.stop()


def test_reset_engine() -> None:

    engine = create_engine()

    engine.start(
        "Runtime"
    )

    engine.reset()

    assert engine.active_session() is None


def test_engine_is_deterministic() -> None:

    engine = create_engine()

    engine.start(
        "Runtime"
    )

    event = Event(
        type=EventType.RUNTIME_EVENT,
        source="runtime",
        data="heartbeat",
    )

    first = engine.execute(
        event
    )

    second = engine.execute(
        event
    )

    assert (
        first.candidate.title
        == second.candidate.title
    )
    