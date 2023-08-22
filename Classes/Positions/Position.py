from __future__ import annotations

from discord import Embed, Interaction
from typing import TYPE_CHECKING, Optional, Tuple, Type, TypeVar
from uuid import UUID

from UI import CloseMessageView
from UI.Positions import *
from Utils import NS, Utilities

if TYPE_CHECKING:
    from Classes import DeadBot, GuildData
################################################################################

__all__ = ("Position", )

P = TypeVar("P", bound="Position")

################################################################################
class Position:

    __slots__ = (
        "_parent",
        "_id",
        "_name",
        "_description",
        "_salary",
        "_enabled",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(
        self,
        parent: GuildData,
        _id: UUID,
        name: str,
        description: Optional[str],
        salary: int,
        enabled: bool
    ):

        self._parent: GuildData = parent
        self._id: UUID = _id

        self._name: str = name
        self._description: Optional[str] = description
        self._salary: int = salary
        self._enabled: bool = enabled

################################################################################
    @classmethod
    def new(
        cls: Type[P],
        guild: GuildData,
        name: str,
        salary: int,
        description: Optional[str]
    ) -> P:

        return cls(
            parent=guild,
            _id=guild.bot.database.insert.position(guild, name, description, salary),
            name=name,
            description=description,
            salary=salary,
            enabled=True
        )

################################################################################
    @classmethod
    def load(cls: Type[P], guild: GuildData, data: Tuple[str, int, str, Optional[str], int, bool]) -> P:

        return cls(
            parent=guild,
            _id=UUID(data[0]),
            name=data[2],
            description=data[3],
            salary=data[4],
            enabled=data[5]
        )

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def bot(self) -> DeadBot:

        return self._parent.bot

################################################################################
    @property
    def id(self) -> UUID:

        return self._id

################################################################################
    @property
    def name(self) -> str:

        return self._name

################################################################################
    @property
    def description(self) -> Optional[str]:

        return self._description

################################################################################
    @property
    def salary(self) -> int:

        return self._salary

################################################################################
    @property
    def enabled(self) -> bool:

        return self._enabled

################################################################################
    @enabled.setter
    def enabled(self, value: bool) -> None:

        self._enabled = value
        self.update()

################################################################################
##### METHODS ##################################################################
################################################################################
    def update(self) -> None:

        self.bot.database.update.position(self)

################################################################################
    async def set_values(self, interaction: Interaction) -> None:

        modal = PositionDataModal(self)

        await interaction.response.send_modal(modal)
        await modal.wait()

        if not modal.complete:
            return

        self._name, self._salary, self._description = modal.value
        self.update()

        confirm = self.status()
        confirm.title = "Position Updated"
        view = CloseMessageView(interaction.user)

        await interaction.followup.send(embed=confirm, view=view)
        await view.wait()

################################################################################
    def status(self) -> Embed:

        description = (
            "\n".join(Utilities.wrap_text(self.description, 30))
            if self.description else str(NS)
        )
        return Utilities.make_embed(
            title="Position Status",
            description=(
                f"__**Name:**__ `{self.name}`\n"
                f"__**Salary:**__ `{self.salary:,} gil`\n"
                "__**Description:**__\n"
                f"{description}\n"
                f"{Utilities.draw_line(extra=30)}"
            ),
            footer_text=(
                "This position is currently " +
                ("enabled." if self.enabled else "disabled.")
            )
        )

################################################################################
