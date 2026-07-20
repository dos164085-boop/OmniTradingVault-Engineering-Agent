"""
Runtime Service.

Public application service for the Runtime subsystem.

The RuntimeService coordinates engineering sessions and delegates
event processing to the RuntimePipeline.

This class represents the public API exposed by the Runtime.
"""

from __future__ import annotations

from src.runtime.managers.session_manager import SessionManager
from src.runtime.models import (
    Event,
    RuntimeResult,
    Session,
)
from src.runtime.runtime_pipeline import RuntimePipeline


class RuntimeService:
    """
    Public Runtime application service.

    Coordinates Runtime execution without implementing
    engineering business logic.
    """

    def __init__(
        self,
    ) -> None:

        self._pipeline = RuntimePipeline()

        self._session_manager = SessionManager()

    @property
    def pipeline(
        self,
    ) -> RuntimePipeline:
        """
        Return the RuntimePipeline.
        """

        return self._pipeline

    @property
    def session_manager(
        self,
    ) -> SessionManager:
        """
        Return the SessionManager.
        """

        return self._session_manager

    def start_session(
        self,
        title: str,
    ) -> Session:
        """
        Create and activate a Runtime session.
        """

        return self._session_manager.create_session(
            title
        )

    def active_session(
        self,
    ) -> Session | None:
        """
        Return the active Runtime session.
        """

        return (
            self._session_manager.get_active_session()
        )

    def execute(
        self,
        event: Event,
    ) -> RuntimeResult:
        """
        Execute a Runtime event.

        Raises:
            RuntimeError:
                If there is no active engineering session.
        """

        if (
            not self._session_manager.has_active_session()
        ):
            raise RuntimeError(
                "No active engineering session."
            )

        return self._pipeline.process(
            event
        )

    def close_session(
        self,
    ) -> Session:
        """
        Close the active Runtime session.
        """

        session = self.active_session()

        if session is None:
            raise RuntimeError(
                "No active engineering session."
            )

        return self._session_manager.close_session(
            session.id
        )

    def reset(
        self,
    ) -> None:
        """
        Reset the Runtime state.
        """

        self._pipeline.clear()

        self._session_manager.clear()