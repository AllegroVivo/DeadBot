from __future__ import annotations

from discord import Interaction, User
from typing import TYPE_CHECKING, List, Optional

from .Game import SubnauticaGame
from .Lobby import SubnauticaLobby
from .Player import SubnauticaPlayer

from Utils import *

if TYPE_CHECKING:
    from Classes import DeadBot
################################################################################

__all__ = ("SubnauticaLobbyManager",)

################################################################################
class SubnauticaLobbyManager:

    __slots__ = (
        "_state",
        "_players",
        "_lobbies",
    )

################################################################################
    def __init__(self, bot: DeadBot):

        self._state: DeadBot = bot
        self._players: List[SubnauticaPlayer]
        self._lobbies: List[SubnauticaLobby] = []

################################################################################
    @property
    def bot(self) -> DeadBot:

        return self._state

################################################################################
    async def new_game(self, interaction: Interaction) -> None:

        player = self.get_player_by_user(interaction.user)
        if player is None:
            player = SubnauticaPlayer(interaction.user)
            self._players.append(player)

        game = self.get_game_by_player(player)
        if game is not None:
            error = AlreadyInGameError(player, game)
            await interaction.response.send_message(embed=error, ephemeral=True)
            return

        self._lobbies.append(SubnauticaLobby(self, player))
        await dummy_response(interaction)

################################################################################
    def get_player_by_user(self, user: User) -> Optional[SubnauticaPlayer]:

        for player in self._players:
            if player.user.id == user.id:
                return player

################################################################################
    def get_game_by_player(self, player: SubnauticaPlayer) -> Optional[SubnauticaGame]:

        for lobby in self._lobbies:
            if player in lobby.players:
                return lobby.game

################################################################################
