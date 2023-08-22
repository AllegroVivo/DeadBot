from __future__ import annotations

import asyncio

from discord import Message, User, Interaction
from typing import TYPE_CHECKING, List, Optional, Dict, Union, Any
from uuid import UUID, uuid4

from discord.ui import View

from .Creature import CreatureCard
from .Equipment import EquipmentCard
from .GameLog import SubnauticaGameLog
from .LogItem import SubnauticaLogItem
from .MessageMgr import GameMessageManager
from .Player import SubnauticaPlayer
from .Resource import ResourceCard
from .Turn import SubnauticaTurn
from .DeckMgr import DeckManager

from UI.Game import ActivePlayerView, InactivePlayerView
from Utils import *

if TYPE_CHECKING:
    from Classes import DeadBot
################################################################################

__all__ = ("SubnauticaGame",)

################################################################################
class SubnauticaGame:

    __slots__ = (
        "_state",
        "_id",
        "_players",
        "_turn",
        "_decks",
        "_log",
    )

################################################################################
    def __init__(self, bot: DeadBot, players: List[SubnauticaPlayer]):

        self._state: DeadBot = bot
        self._id: UUID = uuid4()

        self._players: List[SubnauticaPlayer] = players
        self._turn: SubnauticaTurn = SubnauticaTurn(self)

        self._decks: DeckManager = DeckManager(self)
        self._log: SubnauticaGameLog = SubnauticaGameLog(self)

################################################################################
    def __eq__(self, other: SubnauticaGame) -> bool:

        return self.id == other.id

################################################################################
    @property
    def bot(self) -> DeadBot:

        return self._state

################################################################################
    @property
    def id(self) -> UUID:

        return self._id

################################################################################
    @property
    def players(self) -> List[SubnauticaPlayer]:

        return self._players

################################################################################
    @property
    def current_player(self) -> SubnauticaPlayer:

        return self._players[self._turn.current_player.value]

################################################################################
    @property
    def turn(self) -> int:

        return self._turn.turn

################################################################################
    @property
    def log(self) -> SubnauticaGameLog:

        return self._log

################################################################################
    @property
    def deck_manager(self) -> DeckManager:

        return self._decks

################################################################################
    @property
    def resource_deck(self) -> List[ResourceCard]:

        return self._decks.resource_deck

################################################################################
    @property
    def creature_deck(self) -> List[CreatureCard]:

        return self._decks.creature_deck

################################################################################
    @property
    def equipment_deck(self) -> List[EquipmentCard]:

        return self._decks.equipment_deck

################################################################################
    async def start(self, interaction: Interaction) -> None:

        # Prepare the cards
        self.deck_manager.shuffle()
        self.deck_manager.deal()

        # Don't forget, we're piggybacking on the interaction from the startup
        # function back in the Lobby, so we need to do a followup here.
        # Which honestly is convenient because now we don't have to include any
        # logic to differentiate between the response and additional followups.
        await interaction.followup.send("Rendering hand images. Please be patient.", delete_after=5)

        # Send a "Game Log" message to the channel first so it's above the players' hands.
        log_msg = await interaction.followup.send(embed=self.log.message)
        await self.log.set_game_log_message(log_msg)

        self.log.log(SubnauticaLogItem(self.players[0], LogAction.GameStart))

        # Start the main loop.
        await self.run_turn(interaction)

################################################################################
    async def run_turn(self, interaction: Interaction) -> None:

        # TODO: Render and dump player hand images for sending

        # Send the player "Hand" messages.
        # We can maintain all of them as persistent messages, so we don't have to
        # worry about deleting or any potential confusion resulting from more
        # than one 'hand' being present in the game channel.
        async def send_message(p):
            """Coro that sends a new ephemeral 'hand status' message to the
            provided player."""
            hand = GameMessageManager.card_hand(p, self._turn)
            view = (InactivePlayerView if not p.is_active else ActivePlayerView)(p)
            message = await interaction.followup.send(embed=hand, view=view, ephemeral=True)

            p.hand = message
            p.view = view

        async def cancel_player_views(active_player: View, views: List[View]):
            """Coro that waits for the active player to make their move, then cancels
            all other views without blocking game execution."""
            await active_player.wait()
            # Note: Blocking occurs here because of the wait call, which means that once
            # the active player's view is stopped, the other views will stop and the
            # game will continue.
            await asyncio.gather(*(view.stop() for view in views if view != active_player))

        # Send all messages concurrently
        await asyncio.gather(*(send_message(p) for p in self.players))

        player_views = [p.view for p in self.players]
        active_view = next(view for view in player_views if view.is_active)

        # Start the background task that will stop all views except the active one
        asyncio.create_task(cancel_player_views(active_view, player_views))
        # Wait for all views concurrently
        await asyncio.gather(*(view.wait() for view in player_views if view != active_view))

        # Once all views have stopped (ie. `cancel_player_views` has returned), we can
        # continue with the game by handling the value returned by the active
        # player's view selection.

################################################################################
