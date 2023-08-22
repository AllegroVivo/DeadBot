from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, List, Optional

from discord import Interaction

from UI.Game import ConfirmGameStartView
from .Game import SubnauticaGame
from .MessageMgr import GameMessageManager

if TYPE_CHECKING:
    from Classes import DeadBot, SubnauticaPlayer, SubnauticaLobbyManager
################################################################################

__all__ = ("SubnauticaLobby",)

################################################################################
class SubnauticaLobby:

    __slots__ = (
        "_state",
        "_manager",
        "_owner",
        "_players",
        "_join_link",
        "_game",
    )

################################################################################
    def __init__(self, manager: SubnauticaLobbyManager, player: SubnauticaPlayer):

        self._state: DeadBot = manager.bot
        self._manager: SubnauticaLobbyManager = manager

        self._owner: SubnauticaPlayer = player
        self._players: List[SubnauticaPlayer] = [player]

        self._game: Optional[SubnauticaGame] = None
        self._join_link: Optional[str] = None  # type: ignore

################################################################################
    @property
    def owner(self) -> SubnauticaPlayer:

        return self._owner

################################################################################
    @property
    def game(self) -> Optional[SubnauticaGame]:

        return self._game

################################################################################
    @property
    def players(self) -> List[SubnauticaPlayer]:

        return self._players

################################################################################
    @property
    def join_link(self) -> Optional[str]:

        return self._join_link

################################################################################
    async def game_start(self, interaction: Interaction):

        confirm = GameMessageManager.confirm_game_start(self.players)
        view = ConfirmGameStartView(interaction.user, self.players)

        await interaction.response.send_message(embed=confirm, view=view)
        await view.wait()

        if not view.complete:
            return

        if view.value[0] is False:
            embed = GameMessageManager.cancel_game_start()
            await view.value[1].response.send_message(embed=embed, delete_after=7)
            return

        # We've passed the interaction back out of the view so we can defer it
        # below and make it look like the game needs to load.
        inter: Interaction = view.value[1]

        # Give the impression of the game loading. For looks~
        await inter.response.defer()
        await asyncio.sleep(3)

        confirm = GameMessageManager.game_start()
        await interaction.followup.send(embed=confirm, delete_after=5)

        # view.value[0] is True
        self._game = SubnauticaGame(self._state, self.players)

        # Clean up the deferral
        await inter.followup.send("** **", delete_after=0.1)

        # Hand off control to the game
        await self._game.start(interaction)

################################################################################
