"""
Runtime Engine.

Primary entry point of the Runtime subsystem.

The RuntimeEngine exposes a minimal interface for executing
engineering sessions while delegating orchestration to the
RuntimeService.
"""

from __future__ import annotations

from src.runtime.models import (
    Event,
    RuntimeResult,
    Session,
)
from src.runtime.services.runtime_service import (
    RuntimeService,
)


class RuntimeEngine:
    """
    Primary Runtime entry point.

    The RuntimeEngine delegates all execution to the RuntimeService
    and exposes a simple API for higher-level components such as
    MECA.
    """

    def __init__(
        self,
    ) -> None:

        self._service = RuntimeService()

    @property
    def service(
        self,
    ) -> RuntimeService:
        """
        Return the RuntimeService.
        """

        return self._service

    def start(
        self,
        title: str,
    ) -> Session:
        """
        Start a new engineering session.
        """

        return self._service.start_session(
            title
        )

    def active_session(
        self,
    ) -> Session | None:
        """
        Return the active engineering session.
        """

        return self._service.active_session()

    def execute(
        self,
        event: Event,
    ) -> RuntimeResult:
        """
        Execute a Runtime event.
        """

        return self._service.execute(
            event
        )

    def stop(
        self,
    ) -> Session:
        """
        Stop the active engineering session.
        """

        return self._service.close_session()

    def reset(
        self,
    ) -> None:
        """
        Reset the Runtime state.
        """

        self._service.reset()