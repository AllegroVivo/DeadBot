from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Classes import DeadBot, Database
################################################################################

__all__ = ("DBWorkerBranch",)

################################################################################
class DBWorkerBranch:

    __slots__ = (
        "_state",
    )

################################################################################
    def __init__(self, _state: DeadBot):

        self._state: DeadBot = _state

################################################################################
    @property
    def bot(self) -> DeadBot:

        return self._state

################################################################################
    @property
    def database(self) -> Database:

        return self._state.database

################################################################################
