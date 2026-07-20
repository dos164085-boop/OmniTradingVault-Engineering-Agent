"""
Tests for the RuntimeService component.
"""

from __future__ import annotations

import pytest

from src.runtime.models import (
    Event,
    EventType,
    RuntimeResult,
    Session,
)
from src.runtime.services.runtime_service import (
    RuntimeService,
)


def create_service() -> RuntimeService:
    """
    Build a RuntimeService for testing.
    """

    return RuntimeService()


def test_start_session() -> None:

    service = create_service()

    session = service.start_session(
        "Runtime Session"
    )

    assert isinstance(
        session,
        Session,
    )

    assert (
        service.active_session()
        is not None
    )


def test_execute_event() -> None:

    service = create_service()

    service.start_session(
        "Runtime"
    )

    event = Event(
        type=EventType.RUNTIME_EVENT,
        source="runtime",
        data="heartbeat",
    )

    result = service.execute(
        event
    )

    assert isinstance(
        result,
        RuntimeResult,
    )

    assert (
        result.event
        == event
    )


def test_execute_without_session_should_fail() -> None:

    service = create_service()

    event = Event(
        type=EventType.RUNTIME_EVENT,
        source="runtime",
        data="heartbeat",
    )

    with pytest.raises(
        RuntimeError
    ):

        service.execute(
            event
        )


def test_close_session() -> None:

    service = create_service()

    service.start_session(
        "Runtime"
    )

    session = service.close_session()

    assert (
        session.is_active()
        is False
    )

    assert (
        service.active_session()
        is None
    )


def test_close_without_session_should_fail() -> None:

    service = create_service()

    with pytest.raises(
        RuntimeError
    ):

        service.close_session()


def test_reset() -> None:

    service = create_service()

    service.start_session(
        "Runtime"
    )

    service.reset()

    assert (
        service.active_session()
        is None
    )


def test_service_is_deterministic() -> None:

    service = create_service()

    service.start_session(
        "Runtime"
    )

    event = Event(
        type=EventType.RUNTIME_EVENT,
        source="runtime",
        data="heartbeat",
    )

    first = service.execute(
        event
    )

    second = service.execute(
        event
    )

    assert (
        first.candidate.title
        == second.candidate.title
    )
    