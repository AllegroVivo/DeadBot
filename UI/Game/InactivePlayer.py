from __future__ import annotations

from discord import Interaction, User, ButtonStyle
from typing import TYPE_CHECKING, List, Optional

from discord.ui import Button

from UI.View import FroggeView

if TYPE_CHECKING:
    from Classes import SubnauticaPlayer, GameMessageManager
################################################################################

__all__ = ("InactivePlayerView",)

################################################################################
class InactivePlayerView(FroggeView):

    def __init__(self, owner: SubnauticaPlayer):

        super().__init__(owner.user)

        self.is_active = False

        component_list = [
            TurnHelpButton(),
            CardHelpButton(),
        ]

        for item in component_list:
            self.add_item(item)

################################################################################
class TurnHelpButton(Button):

    def __init__(self):

        super().__init__(
            style=ButtonStyle.blurple,
            label="Turn Help",
            disabled=False,
            row=0,
            emoji="🔁"
        )

    async def callback(self, interaction: Interaction):
        embed = GameMessageManager.turn_help()
        await interaction.response.send_message(embed=embed, ephemeral=True)

################################################################################
class CardHelpButton(Button):

    def __init__(self):

        super().__init__(
            style=ButtonStyle.blurple,
            label="Card Help",
            disabled=False,
            row=0,
            emoji="🃏"
        )

    async def callback(self, interaction: Interaction):
        embed = GameMessageManager.card_help()
        await interaction.response.send_message(embed=embed, ephemeral=True)

################################################################################
