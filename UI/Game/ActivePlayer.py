from __future__ import annotations

from discord import Interaction, User, ButtonStyle
from typing import TYPE_CHECKING, List, Optional

from discord.ui import Button

from UI.View import FroggeView

if TYPE_CHECKING:
    from Classes import SubnauticaPlayer, GameMessageManager
################################################################################

__all__ = ("ActivePlayerView",)

################################################################################
class ActivePlayerView(FroggeView):

    def __init__(self, owner: SubnauticaPlayer):

        super().__init__(owner.user)

        self.is_active = True

        component_list = [

        ]

        for item in component_list:
            self.add_item(item)

################################################################################
