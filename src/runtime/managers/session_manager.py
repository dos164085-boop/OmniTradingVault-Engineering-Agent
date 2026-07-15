"""
Session Manager.

Coordinates the lifecycle of engineering sessions during Runtime
execution.

The SessionManager owns runtime sessions and synchronizes the active
session with WorkingMemory.

This component never communicates directly with the Knowledge Core.
"""

from __future__ import annotations

from uuid import UUID

from src.runtime.models.session import Session
from src.runtime.working_memory import WorkingMemory


class SessionManager:
    """
    Coordinates engineering sessions.
    """

    ACTIVE_SESSION_KEY = "runtime.active_session"

    def __init__(
        self,
        working_memory: WorkingMemory,
    ) -> None:
        self._working_memory = working_memory
        self._sessions: dict[UUID, Session] = {}

    def create_session(
        self,
        title: str,
    ) -> Session:
        """
        Create and activate a new engineering session.
        """

        if self.has_active_session():
            raise RuntimeError(
                "An active engineering session already exists."
            )

        session = Session(title=title)

        self._sessions[session.id] = session

        self._working_memory.set(
            self.ACTIVE_SESSION_KEY,
            session.id,
        )

        return session

    def get_session(
        self,
        session_id: UUID,
    ) -> Session:
        """
        Retrieve a session by its identifier.
        """

        if session_id not in self._sessions:
            raise KeyError(
                f"Unknown session '{session_id}'."
            )

        return self._sessions[session_id]

    def get_active_session(self) -> Session | None:
        """
        Return the current active session.
        """

        session_id = self._working_memory.get(
            self.ACTIVE_SESSION_KEY
        )

        if session_id is None:
            return None

        return self._sessions.get(session_id)

    def has_active_session(self) -> bool:
        """
        Return True if an active session exists.
        """

        session = self.get_active_session()

        return (
            session is not None
            and session.is_active()
        )

    def close_session(
        self,
        session_id: UUID,
    ) -> Session:
        """
        Close a session.
        """

        session = self.get_session(session_id)

        session.close()

        active = self._working_memory.get(
            self.ACTIVE_SESSION_KEY
        )

        if active == session.id:
            self._working_memory.remove(
                self.ACTIVE_SESSION_KEY
            )

        return session

    def add_decision(
        self,
        session_id: UUID,
        decision_id: UUID,
    ) -> None:
        """
        Associate a decision with a session.
        """

        session = self.get_session(session_id)

        session.add_decision(decision_id)

    def list_sessions(self) -> list[Session]:
        """
        Return all sessions.
        """

        return list(self._sessions.values())

    def session_count(self) -> int:
        """
        Return the number of managed sessions.
        """

        return len(self._sessions)

    def clear(self) -> None:
        """
        Clear manager state.

        Intended only for testing.
        """

        self._sessions.clear()

        self._working_memory.remove(
            self.ACTIVE_SESSION_KEY
        )
        