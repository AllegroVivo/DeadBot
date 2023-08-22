from __future__ import annotations

from discord import InputTextStyle, Interaction, User, ComponentType
from discord.ui import InputText, Select
from typing import TYPE_CHECKING, Any, List, Optional, Tuple

import Utils
from UI import FroggeView, CloseMessageButton
from UI.Modal import FroggeModal
from Utils import TimeZone, Pronoun

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("SetPronounsView",)

################################################################################
class SetPronounsView(FroggeView):

    def __init__(self, owner: User):

        super().__init__(owner=owner, close_on_complete=True)

        self.add_item(SetPronounsSelect())
        self.add_item(CloseMessageButton())

################################################################################
class SetPronounsSelect(Select):

    def __init__(self):

        super().__init__(
            select_type=ComponentType.string_select,
            placeholder="Select your pronouns...",
            options=Pronoun.select_options(),
            max_values=len(Pronoun.select_options()),
            disabled=False,
            row=0
        )

    async def callback(self, interaction: Interaction):
        self.view.value = [Pronoun(int(v)) for v in self.values]
        self.view.complete = True

        await Utils.dummy_response(interaction)
        await self.view.stop()  # type: ignore

################################################################################
