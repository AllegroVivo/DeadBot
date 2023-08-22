from __future__ import annotations

from discord import Interaction
from typing import TYPE_CHECKING, Any, List, Optional, Tuple, TypeVar, Type, Union

from .Position import Position
from UI import CloseMessageView
from UI.Positions import *
from Utils import *

if TYPE_CHECKING:
    from uuid import UUID

    from Classes import GuildData, DeadBot
################################################################################

__all__ = ("PositionManager",)

PM = TypeVar("PM", bound="PositionManager")

################################################################################
class PositionManager:

    __slots__ = (
        "_parent",
        "_positions",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, guild: GuildData, positions: Optional[List[Position]] = None):

        self._parent: GuildData = guild

        self._positions: List[Position] = positions
        if self._positions is None:
            self._positions = []

################################################################################
    @classmethod
    def load_from_data(
        cls: Type[PM],
        guild: GuildData,
        data: List[Tuple[str, int, str, Optional[str], int, bool]]
    ) -> PM:

        return cls(
            guild=guild,
            positions=[Position.load(guild, position) for position in data]
        )

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def bot(self) -> DeadBot:

        return self._parent.bot

################################################################################
##### METHODS ##################################################################
################################################################################
    def get_position(self, name: str) -> Optional[Position]:

        for position in self._positions:
            if position.name.lower() == name.lower():
                return position

################################################################################
    def get_position_by_id(self, _id: UUID) -> Optional[Position]:

        for position in self._positions:
            if position.id == _id:
                return position

################################################################################
    async def fetch_position(self, interaction: Interaction) -> Optional[Union[Position, Interaction]]:

        print("Fetching position...")
        modal = PositionNameModal()

        print("Sending modal...")
        await interaction.response.send_modal(modal)
        await modal.wait()

        print("Modal complete...")
        if not modal.complete:
            return

        print("Getting position...")
        print(f"Name: {modal.value[0]}")
        print(self._positions)
        position = self.get_position(modal.value[0])
        if position is None:
            error = PositionNotFoundError(modal.value[0])
            await interaction.followup.send(embed=error, ephemeral=True)
            return

        return position, modal.value[1]  # type: ignore

################################################################################
    async def add_position(self, interaction: Interaction) -> None:

        modal = PositionDataModal()

        await interaction.response.send_modal(modal)
        await modal.wait()

        if not modal.complete:
            return

        name, salary, description = modal.value
        new_position = Position.new(self._parent, name, salary, description)
        self._positions.append(new_position)

        confirm = new_position.status()
        confirm.title = "Position Added"
        view = CloseMessageView(interaction.user)

        await interaction.followup.send(embed=confirm, view=view)
        await view.wait()

################################################################################
    async def toggle_position(self, interaction: Interaction) -> None:

        response = await self.fetch_position(interaction)
        if response is None:
            return

        position, _ = response
        position.enabled = not position.enabled

        confirm = position.status()
        confirm.title = "Position Toggled"
        view = CloseMessageView(interaction.user)

        await interaction.followup.send(embed=confirm, view=view)
        await view.wait()

################################################################################
    async def edit_position(self, interaction: Interaction) -> None:

        response = await self.fetch_position(interaction)
        if response is None:
            return

        position, inter = response
        await position.set_values(inter)

################################################################################
