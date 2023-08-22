from __future__ import annotations

from discord import User, Interaction, ButtonStyle
from discord.ui import Button
from typing import TYPE_CHECKING, List, Optional

from Assets import BotEmojis
from UI.View import FroggeView
from Utils import *

if TYPE_CHECKING:
    from Classes import SubnauticaPlayer
################################################################################

__all__ = ("ConfirmGameStartView",)

################################################################################
class ConfirmGameStartView(FroggeView):

    def __init__(self, owner: User, players: List[SubnauticaPlayer]):

        super().__init__(owner, close_on_complete=True)

        component_list = [
            ConfirmGameStartButton(),
            CancelGameStartButton(len(players)),
        ]

        for item in component_list:
            self.add_item(item)

################################################################################
class ConfirmGameStartButton(Button):

    def __init__(self):

        super().__init__(
            style=ButtonStyle.success,
            label="We're Ready to Start!",
            disabled=False,
            row=0,
            emoji=BotEmojis.Check
        )

    async def callback(self, interaction: Interaction):
        self.view.value = True, interaction
        self.view.complete = True

        # No dummy response here. Packaging the interaction into the return value.
        await self.view.stop()  # type: ignore

################################################################################

class CancelGameStartButton(Button):

    def __init__(self, num_players: int):

        super().__init__(
            style=ButtonStyle.danger,
            label="Wait! Hang on! Not Yet~!",
            disabled=num_players > 1,
            row=0,
            emoji=BotEmojis.Cross
        )

    async def callback(self, interaction: Interaction):
        self.view.value = False, interaction
        self.view.complete = True

        # No dummy response here. Packaging the interaction into the return value.
        await self.view.stop()  # type: ignore

################################################################################
