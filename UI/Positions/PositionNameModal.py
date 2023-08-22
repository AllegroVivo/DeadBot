from __future__ import annotations

from typing import TYPE_CHECKING

from discord import InputTextStyle, Interaction
from discord.ui import InputText

from UI.Modal import FroggeModal
from Utils import *

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("PositionNameModal",)

################################################################################
class PositionNameModal(FroggeModal):

    def __init__(self):

        super().__init__(title="Enter Position Name")

        self.add_item(
            InputText(
                style=InputTextStyle.singleline,
                label="Instructions",
                placeholder="Enter the name of the position to edit.",
                value="Enter the name of the position to edit.",
                required=False
            )
        )

        self.add_item(
            InputText(
                style=InputTextStyle.singleline,
                label="Position Name",
                placeholder="Enter the name of the position to edit.",
                required=True
            )
        )

    async def callback(self, interaction: Interaction):
        self.value = self.children[1].value, interaction
        self.complete = True

        # No dummy response so we can pass the interaction back outside this modal.
        self.stop()

################################################################################
