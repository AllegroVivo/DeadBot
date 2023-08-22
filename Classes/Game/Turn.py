from __future__ import annotations

from discord import Interaction
from typing import TYPE_CHECKING, List, Optional

from Utils import *

if TYPE_CHECKING:
    from Classes import SubnauticaGame
################################################################################

__all__ = ("SubnauticaTurn",)

################################################################################
class SubnauticaTurn:

    __slots__ = (
        "_game",
        "_player",
        "_turn",
    )

################################################################################
    def __init__(self, game: SubnauticaGame):

        self._game: SubnauticaGame = game
        self._player: Player = Player.Player1
        self._turn: int = 1

################################################################################
    @property
    def game(self) -> SubnauticaGame:

        return self._game

################################################################################
    @property
    def current_player(self) -> Player:

        return self._player

################################################################################
    @property
    def turn(self) -> int:

        return self._turn

################################################################################
