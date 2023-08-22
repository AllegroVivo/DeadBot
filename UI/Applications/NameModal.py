from __future__ import annotations

from discord import InputTextStyle, Interaction, User
from discord.ui import InputText
from typing import TYPE_CHECKING, Any, List, Optional, Tuple

import Utils
from UI.Modal import FroggeModal

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("SetNameModal",)

################################################################################
class SetNameModal(FroggeModal):

    def __init__(self, cur_val: Optional[str]):

        super().__init__(title="Set Name")

        self.add_item(
            InputText(
                style=InputTextStyle.multiline,
                label="Instructions",
                placeholder="Enter your name below...",
                value="(Required) Please enter your character's name below.",
                required=False
            )
        )
        self.add_item(
            InputText(
                style=InputTextStyle.singleline,
                label="Name",
                placeholder="Enter your name here",
                value=cur_val,
                max_length=25,
                required=True
            )
        )

    async def callback(self, interaction: Interaction):
        self.value = self.children[1].value
        self.complete = True

        await Utils.dummy_response(interaction)
        self.stop()

################################################################################
