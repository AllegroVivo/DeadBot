from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, Type, TypeVar, Any, Dict
from uuid import UUID, uuid4

from discord import User, Interaction

from .Details import ApplicationDetails
from .Experience import ApplicationExperience
from .AppMessageMgr import ApplicationMessageManager
from UI.Applications import ApplicationStatusView
from Utils import *

if TYPE_CHECKING:
    from Classes import DeadBot, Position, ApplicationManager, PriorWorkExp, GuildData
################################################################################

__all__ = ("Application", )

A = TypeVar("A", bound="Application")

################################################################################
class Application:

    __slots__ = (
        "_manager",
        "_id",
        "_user",
        "_positions",
        "_details",
        "_experience",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, manager: ApplicationManager, user: User, _id: UUID, **kwargs):

        self._manager: ApplicationManager = manager
        self._id: UUID = _id
        self._user: User = user

        self._positions: List[Position] = kwargs.pop("positions", None) or []
        self._details: ApplicationDetails = kwargs.pop("details", None) or ApplicationDetails(self)
        self._experience: ApplicationExperience = kwargs.pop("experience", None) or ApplicationExperience(self)

################################################################################
    @classmethod
    def new(cls: Type[A], manager: ApplicationManager, user: User) -> A:

        _id = manager.bot.database.insert.application(manager._state, user)
        return cls(manager, user, _id)

################################################################################
    @classmethod
    def load(
        cls: Type[A],
        guild: GuildData,
        user: User,
        app_id: str,
        record: Dict[str, Any]
    ) -> A:

        self: A = cls.__new__(cls)

        self._manager = guild.application_manager
        self._user = user
        self._id = UUID(app_id)

        self._positions = [
            guild.position_manager.get_position_by_id(_id) for _id in record["Main"][3]
        ]
        self._details = ApplicationDetails.load(self, record["Main"])
        self._experience = ApplicationExperience.load(self, record)

        return self

################################################################################
    @property
    def id(self) -> UUID:

        return self._id

################################################################################
    @property
    def user(self) -> User:

        return self._user

################################################################################
    @property
    def positions(self) -> List[Position]:

        return self._positions

################################################################################
    @property
    def name(self) -> Optional[str]:

        return self._details.name

################################################################################
    @property
    def age(self) -> Optional[int]:

        return self._details.age

################################################################################
    @property
    def timezone(self) -> TimeZone:

        return self._details.timezone

################################################################################
    @property
    def pronouns(self) -> List[Pronoun]:

        return self._details.pronouns

################################################################################
    @property
    def languages(self) -> List[Language]:

        return self._details.languages

################################################################################
    @property
    def datacenter(self) -> DataCenter:

        return self._details.datacenter

################################################################################
    @property
    def world(self) -> WorldEnum:

        return self._details.world

################################################################################
    @property
    def about(self) -> Optional[str]:

        return self._details.about

################################################################################
    @property
    def image(self) -> Optional[str]:

        return self._details.image

################################################################################
    @property
    def notes(self) -> Optional[str]:

        return self._details.notes

################################################################################
    @property
    def approved(self) -> Optional[bool]:

        return self._details.approved

################################################################################
    @property
    def work_experience(self) -> List[PriorWorkExp]:

        return self._experience.work_experience

################################################################################
    @property
    def rp_choice(self) -> bool:

        return self._experience.rp_choice

################################################################################
    @property
    def rp_level(self) -> RPLevel:

        return self._experience.rp_level

################################################################################
    @property
    def rp_nsfw(self) -> bool:

        return self._experience.rp_nsfw

################################################################################
    @property
    def rp_sample(self) -> Optional[str]:

        return self._experience.rp_sample

################################################################################
    def update(self, exp_updated: bool = False) -> None:

        self._manager.update(self, exp_updated)

################################################################################
    async def resume(self, interaction: Interaction) -> None:

        status = ApplicationMessageManager.application_status(self)
        view = ApplicationStatusView(interaction.user, self)

################################################################################
    async def set_name(self, interaction: Interaction) -> None:

        await self._details.set_name(interaction)

################################################################################
    async def set_age(self, interaction: Interaction) -> None:

        await self._details.set_age(interaction)

################################################################################
    async def set_timezone(self, interaction: Interaction) -> None:

        await self._details.set_timezone(interaction)

################################################################################
    async def set_pronouns(self, interaction: Interaction) -> None:

        await self._details.set_pronouns(interaction)

################################################################################
    async def set_languages(self, interaction: Interaction) -> None:

        await self._details.set_languages(interaction)

################################################################################
    async def set_dcworld(self, interaction: Interaction) -> None:

        await self._details.set_dcworld(interaction)

################################################################################
    async def set_about(self, interaction: Interaction) -> None:

        await self._details.set_about(interaction)

################################################################################
    async def set_notes(self, interaction: Interaction) -> None:

        await self._details.set_notes(interaction)

################################################################################
    async def set_work_experience(self, interaction: Interaction) -> None:

        await self._experience.set_work_experience(interaction)

################################################################################
