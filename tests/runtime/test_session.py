"""
Tests for the Session domain model.
"""

from datetime import datetime
from uuid import UUID

import pytest

from src.runtime.models.session import (
    Session,
    SessionStatus,
)


def test_create_session() -> None:

    session = Session(
        title="Investigate Foundry compiler incompatibility"
    )

    assert isinstance(session.id, UUID)
    assert session.title == (
        "Investigate Foundry compiler incompatibility"
    )
    assert session.status == SessionStatus.ACTIVE
    assert isinstance(session.created_at, datetime)
    assert isinstance(session.updated_at, datetime)
    assert session.decision_ids == []


def test_empty_title_should_fail() -> None:

    with pytest.raises(ValueError):

        Session(title="")


def test_add_decision() -> None:

    session = Session(
        title="Runtime Session"
    )

    decision_id = UUID(
        "11111111-1111-1111-1111-111111111111"
    )

    session.add_decision(
        decision_id
    )

    assert len(session.decision_ids) == 1

    assert session.decision_ids[0] == decision_id


def test_duplicate_decision_is_ignored() -> None:

    session = Session(
        title="Runtime Session"
    )

    decision_id = UUID(
        "11111111-1111-1111-1111-111111111111"
    )

    session.add_decision(decision_id)

    session.add_decision(decision_id)

    assert len(session.decision_ids) == 1


def test_close_session() -> None:

    session = Session(
        title="Runtime Session"
    )

    session.close()

    assert session.status == SessionStatus.CLOSED

    assert session.is_active() is False


def test_closed_session_cannot_receive_decisions() -> None:

    session = Session(
        title="Runtime Session"
    )

    session.close()

    with pytest.raises(ValueError):

        session.add_decision(
            UUID(
                "11111111-1111-1111-1111-111111111111"
            )
        )


def test_is_active() -> None:

    session = Session(
        title="Runtime Session"
    )

    assert session.is_active()

    session.close()

    assert not session.is_active() 