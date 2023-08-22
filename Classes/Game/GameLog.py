from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, List, Optional

from discord import Message, NotFound, Embed

from Utils import LogAction
from .LogItem import SubnauticaLogItem

if TYPE_CHECKING:
    from Classes import SubnauticaGame, SubnauticaPlayer, GameMessageManager
################################################################################

__all__ = ("SubnauticaGameLog",)

################################################################################
class SubnauticaGameLog:

    __slots__ = (
        "_state",
        "_items",
        "_message",
    )

################################################################################
    def __init__(self, game: SubnauticaGame):

        self._state: SubnauticaGame = game

        self._items: List[SubnauticaLogItem] = []
        self._message: Optional[Message] = None

################################################################################
    async def set_game_log_message(self, message: Message):

        if not isinstance(message, Message):
            raise TypeError("Game Log message must be of type discord.Message.")

        await self._fetch_current_log_message()
        if self._message is not None:
            raise RuntimeError("Game Log message already set.")

        self._message = message

################################################################################
    async def _fetch_current_log_message(self) -> None:

        if self._message is None:
            return

        try:
            self._message = await self._message.channel.fetch_message(self._message.id)
        except NotFound:
            self._message = None

################################################################################
    @property
    def message(self) -> Optional[Message]:

        return self._message

################################################################################
    @property
    def items(self) -> List[SubnauticaLogItem]:

        return self._items

################################################################################
    def log(self, item: SubnauticaLogItem) -> None:

        self._items.append(item)

        if self.message is None:
            raise RuntimeError("Game Log message not set.")

        self.update_log_message()

################################################################################
    def update_log_message(self) -> None:

        if self.message is None:
            raise RuntimeError("Game Log message not set.")

        async def message_update() -> None:
            embed = GameMessageManager.game_log(self)
            await self.message.edit(embed=embed)

        asyncio.create_task(message_update())

################################################################################
    def status(self) -> Embed:

        return GameMessageManager.game_log(self)

################################################################################
