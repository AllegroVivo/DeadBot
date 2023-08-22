from __future__ import annotations

from discord import InputTextStyle, Interaction, User, ComponentType
from discord.ui import InputText, Select
from typing import TYPE_CHECKING, Any, List, Optional, Tuple

import Utils
from UI import FroggeView, CloseMessageButton
from UI.Modal import FroggeModal
from Utils import TimeZone

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("SetTimezoneView",)

################################################################################
class SetTimezoneView(FroggeView):

    def __init__(self, owner: User):

        super().__init__(owner=owner, close_on_complete=True)

        self.add_item(SetTimezoneSelect())
        self.add_item(CloseMessageButton())

################################################################################
class SetTimezoneSelect(Select):

    def __init__(self):

        super().__init__(
            select_type=ComponentType.string_select,
            placeholder="Select your timezone...",
            options=TimeZone.select_options(),
            disabled=False,
            row=0
        )

    async def callback(self, interaction: Interaction):
        self.view.value = TimeZone(int(self.values[0]))
        self.view.complete = True

        await Utils.dummy_response(interaction)
        await self.view.stop()  # type: ignore

################################################################################
