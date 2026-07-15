"""
Runtime managers.

Managers coordinate Runtime behavior and orchestrate interactions
between domain models without accessing the Knowledge Core directly.
"""

from .session_manager import SessionManager

__all__ = [
    "SessionManager",
]