"""
Tests for the SessionManager component.
"""

from uuid import UUID

import pytest

from src.runtime.managers.session_manager import SessionManager
from src.runtime.models.session import Session
from src.runtime.working_memory import WorkingMemory


def create_manager() -> SessionManager:
    """
    Build a SessionManager for testing.
    """

    return SessionManager(
        working_memory=WorkingMemory()
    )


def test_create_session() -> None:

    manager = create_manager()

    session = manager.create_session(
        "Investigate compiler incompatibility"
    )

    assert isinstance(session, Session)

    assert manager.session_count() == 1

    assert manager.has_active_session()


def test_get_active_session() -> None:

    manager = create_manager()

    created = manager.create_session(
        "Runtime"
    )

    active = manager.get_active_session()

    assert active is not None

    assert active.id == created.id


def test_create_second_active_session_should_fail() -> None:

    manager = create_manager()

    manager.create_session("Session A")

    with pytest.raises(RuntimeError):

        manager.create_session("Session B")


def test_get_unknown_session_should_fail() -> None:

    manager = create_manager()

    with pytest.raises(KeyError):

        manager.get_session(
            UUID("11111111-1111-1111-1111-111111111111")
        )


def test_close_session() -> None:

    manager = create_manager()

    session = manager.create_session(
        "Runtime"
    )

    manager.close_session(session.id)

    assert manager.has_active_session() is False

    assert manager.get_active_session() is None


def test_add_decision_to_session() -> None:

    manager = create_manager()

    session = manager.create_session(
        "Runtime"
    )

    decision = UUID(
        "22222222-2222-2222-2222-222222222222"
    )

    manager.add_decision(
        session.id,
        decision,
    )

    loaded = manager.get_session(
        session.id
    )

    assert loaded.decision_ids == [
        decision
    ]


def test_list_sessions() -> None:

    manager = create_manager()

    first = manager.create_session(
        "Runtime"
    )

    manager.close_session(
        first.id
    )

    second = manager.create_session(
        "Another session"
    )

    sessions = manager.list_sessions()

    assert len(sessions) == 2

    assert sessions[0].id == first.id

    assert sessions[1].id == second.id


def test_clear_manager() -> None:

    manager = create_manager()

    manager.create_session(
        "Runtime"
    )

    manager.clear()

    assert manager.session_count() == 0

    assert manager.get_active_session() is None
    