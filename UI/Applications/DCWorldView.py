from __future__ import annotations

from discord import InputTextStyle, Interaction, User, ComponentType
from discord.ui import InputText, Select
from typing import TYPE_CHECKING, Any, List, Optional, Tuple

import Utils
from UI import FroggeView, CloseMessageButton
from UI.Modal import FroggeModal
from Utils import TimeZone, Pronoun, Language, DataCenter, get_world_enum

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("SetDCWorldView",)

################################################################################
class SetDCWorldView(FroggeView):

    def __init__(self, owner: User):

        super().__init__(owner=owner, close_on_complete=True)

        self.add_item(SetDatacenterSelect())
        self.add_item(CloseMessageButton())

################################################################################
class SetDatacenterSelect(Select):

    def __init__(self):

        super().__init__(
            select_type=ComponentType.string_select,
            placeholder="Select your Data Center...",
            options=DataCenter.select_options(),
            max_values=len(DataCenter.select_options()),
            disabled=False,
            row=0
        )

    async def callback(self, interaction: Interaction):
        self.view.value = DataCenter(int(self.values[0]))
        self.view.add_item(SetWorldSelect(self.view.value))

        await Utils.edit_message_helper(interaction, view=self.view)

################################################################################
class SetWorldSelect(Select):

    def __init__(self, datacenter: DataCenter):

        world = get_world_enum(datacenter)

        super().__init__(
            select_type=ComponentType.string_select,
            placeholder="Select your World...",
            options=world.select_options(),
            max_values=len(world.select_options()),
            disabled=False,
            row=1
        )

    async def callback(self, interaction: Interaction):
        self.view.value = self.view.value, self.values[0]
        self.view.complete = True

        await Utils.dummy_response(interaction)
        await self.view.stop()  # type: ignore

################################################################################
