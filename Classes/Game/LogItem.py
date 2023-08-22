from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from Utils import *

if TYPE_CHECKING:
    from Classes import DeadBot, SubnauticaPlayer
################################################################################

__all__ = ("SubnauticaLogItem",)

################################################################################
class SubnauticaLogItem:

    __slots__ = (
        "_time",
        "_player",
        "_action",
    )

################################################################################
    def __init__(self, player: SubnauticaPlayer, action: LogAction):

        self._time: datetime = datetime.now()
        self._player: SubnauticaPlayer = player
        self._action: LogAction = action

################################################################################
    def format(self) -> str:

        return (
            f"`[{Utilities.format_dt(self._time, 'T')}] "
            f"{self._player.user.mention:>30}||{self._action.proper_name:<20}`"
        )

################################################################################
