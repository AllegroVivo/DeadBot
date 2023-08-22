from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Classes import DeadBot, SubnauticaPlayer
################################################################################

__all__ = ("SubnauticaPlayerStats",)

################################################################################
class SubnauticaPlayerStats:

    __slots__ = (
        "_player",
        "_games",
        "_resources",
        "_equipment",
        "_creatures",
        "_wins",
        "_points",
    )

################################################################################
    def __init__(self, player: SubnauticaPlayer):

        self._player: SubnauticaPlayer = player
        self._games: int = 0

################################################################################
