from __future__ import annotations

from discord import InputTextStyle, Interaction, User
from discord.ui import InputText
from typing import TYPE_CHECKING, Any, List, Optional, Tuple

import Utils
from UI.Modal import FroggeModal

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("SetAgeModal",)

################################################################################
class SetAgeModal(FroggeModal):

    def __init__(self, cur_val: Optional[str]):

        super().__init__(title="Set Name")

        self.add_item(
            InputText(
                style=InputTextStyle.multiline,
                label="Instructions",
                placeholder="Enter your age below...",
                value=(
                    "(Required) Please enter your age below. This can be "
                    "your real-life age or the age of your character."
                ),
                required=False
            )
        )
        self.add_item(
            InputText(
                style=InputTextStyle.singleline,
                label="Age",
                placeholder="Enter your age here",
                value=cur_val,
                max_length=30,
                required=True
            )
        )

    async def callback(self, interaction: Interaction):
        self.value = self.children[1].value
        self.complete = True

        await Utils.dummy_response(interaction)
        self.stop()

################################################################################
