from __future__ import annotations

from discord import InputTextStyle, Interaction, User
from discord.ui import InputText
from typing import TYPE_CHECKING, Any, List, Optional, Tuple

import Utils
from UI.Modal import FroggeModal

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("SetNotesModal",)

################################################################################
class SetNotesModal(FroggeModal):

    def __init__(self, cur_val: Optional[str]):

        super().__init__(title="Set Name")

        self.add_item(
            InputText(
                style=InputTextStyle.multiline,
                label="Instructions",
                placeholder="Enter your application notes below...",
                value=(
                    "You may optionally enter some notes to include for the owners "
                    "to consider during the application process."
                ),
                required=False
            )
        )
        self.add_item(
            InputText(
                style=InputTextStyle.multiline,
                label="Application Notes",
                placeholder="Enter any notes you have here",
                value=cur_val,
                max_length=250,
                required=False
            )
        )

    async def callback(self, interaction: Interaction):
        self.value = self.children[1].value
        self.complete = True

        await Utils.dummy_response(interaction)
        self.stop()

################################################################################
