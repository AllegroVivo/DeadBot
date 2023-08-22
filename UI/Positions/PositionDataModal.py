from __future__ import annotations

from discord import InputTextStyle, Interaction
from discord.ui import InputText
from typing import TYPE_CHECKING, Optional, Tuple

from UI.Modal import FroggeModal
from Utils import *

if TYPE_CHECKING:
    from Classes import Position
################################################################################

__all__ = ("PositionDataModal",)

################################################################################
class PositionDataModal(FroggeModal):

    def __init__(self, pos: Optional[Position] = None):

        super().__init__(title="Edit Position Data")

        self.add_item(
            InputText(
                style=InputTextStyle.multiline,
                label="Instructions",
                placeholder="Enter the data for this new position.",
                value=(
                    "Enter the data for this new position in the boxes below. "
                    "Salary accepts numbers and 'k'/'m' suffixes only. "
                    "Description is optional, but recommended."
                ),
                required=False
            )
        )

        self.add_item(
            InputText(
                style=InputTextStyle.singleline,
                label="Name",
                placeholder="Enter the name of this new position.",
                value=pos.name if pos else None,
                required=True
            )
        )

        self.add_item(
            InputText(
                style=InputTextStyle.singleline,
                label="Salary",
                placeholder="Enter the salary of this new position.",
                value=f"{pos.salary:,}" if pos else None,
                required=True
            )
        )

        self.add_item(
            InputText(
                style=InputTextStyle.multiline,
                label="Description",
                placeholder="Enter the description of this new position.",
                value=pos.description if pos else None,
                required=False
            )
        )

    async def callback(self, interaction: Interaction):
        salary = Parsers.parse_salary(self.children[2].value)
        if salary is None:
            error = InvalidSalaryError(self.children[2].value)
            await interaction.response.send_message(embed=error, ephemeral=True)
            return

        self.value = self.children[1].value, salary, self.children[3].value
        self.complete = True

        await dummy_response(interaction)
        self.stop()

################################################################################
