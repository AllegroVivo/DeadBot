from __future__ import annotations

from discord import InputTextStyle, Interaction, User
from discord.ui import InputText
from typing import TYPE_CHECKING, Any, List, Optional, Tuple

import Utils
from UI.Modal import FroggeModal

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("SetAboutMeModal",)

################################################################################
class SetAboutMeModal(FroggeModal):

    def __init__(self, cur_val: Optional[str]):

        super().__init__(title="Set Name")

        self.add_item(
            InputText(
                style=InputTextStyle.multiline,
                label="Instructions",
                placeholder="Enter a brief About Me below...",
                value=(
                    "You may optionally enter a brief description of yourself "
                    "here. Not required, but recommended."
                ),
                required=False
            )
        )
        self.add_item(
            InputText(
                style=InputTextStyle.multiline,
                label="About Me",
                placeholder="Enter your About Me here",
                value=cur_val,
                max_length=500,
                required=False
            )
        )

    async def callback(self, interaction: Interaction):
        self.value = self.children[1].value
        self.complete = True

        await Utils.dummy_response(interaction)
        self.stop()

################################################################################
