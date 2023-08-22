from __future__ import annotations

from typing import TYPE_CHECKING, Any, Tuple, Optional, List, Type, TypeVar

from discord import Interaction

from UI.Applications import *
from Utils import *

if TYPE_CHECKING:
    from Classes import DeadBot, Application, ApplicationMessageManager
################################################################################

__all__ = ("ApplicationDetails",)

AD = TypeVar("AD", bound="ApplicationDetails")

################################################################################
class ApplicationDetails:

    __slots__ = (
        "_parent",
        "_name",
        "_age",
        "_timezone",
        "_pronouns",
        "_languages",
        "_datacenter",
        "_world",
        "_about",
        "_image",
        "_notes",
        "_approved",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, parent: Application, **kwargs):

        self._parent: Application = parent

        self._name: Optional[str] = kwargs.get("name", None)
        self._age: Optional[str] = kwargs.get("age", None)
        self._timezone: TimeZone = kwargs.get("timezone", None) or TimeZone.Null
        self._pronouns: List[Pronoun] = kwargs.get("pronouns", None) or []
        self._languages: List[Language] = kwargs.get("languages", None) or []
        self._datacenter: DataCenter = kwargs.get("datacenter", None) or DataCenter.Null
        self._world: WorldEnum = kwargs.get("world", None) or AetherWorld.Null
        self._about: Optional[str] = kwargs.get("about", None)
        self._image: Optional[str] = kwargs.get("image", None)
        self._notes: Optional[str] = kwargs.get("notes", None)
        self._approved: Optional[bool] = kwargs.get("approved", None)

################################################################################
    @classmethod
    def load(cls: Type[AD], parent: Application, data: Tuple[Any, ...]) -> AD:

        return cls(
            parent=parent,
            name=data[4],
            age=data[5],
            timezone=TimeZone(data[6]),
            pronouns=[Pronoun(i) for i in data[7]],
            languages=[Language(i) for i in data[8]],
            datacenter=DataCenter(data[9]),
            world=world_enum_factory(data[10]),
            about=data[11],
            image=data[12],
            notes=data[13],
            approved=data[14],
        )

################################################################################
    @property
    def application(self) -> Application:

        return self._parent

################################################################################
    @property
    def name(self) -> Optional[str]:

        return self._name

################################################################################
    @property
    def age(self) -> Optional[str]:

        return self._age

################################################################################
    @property
    def timezone(self) -> TimeZone:

        return self._timezone

################################################################################
    @property
    def pronouns(self) -> List[Pronoun]:

        return self._pronouns

################################################################################
    @property
    def languages(self) -> List[Language]:

        return self._languages

################################################################################
    @property
    def datacenter(self) -> DataCenter:

        return self._datacenter

################################################################################
    @property
    def world(self) -> WorldEnum:

        return self._world

################################################################################
    @property
    def about(self) -> Optional[str]:

        return self._about

################################################################################
    @property
    def image(self) -> Optional[str]:

        return self._image

################################################################################
    @property
    def notes(self) -> Optional[str]:

        return self._notes

################################################################################
    @property
    def approved(self) -> Optional[bool]:

        return self._approved

################################################################################
    def update(self) -> None:

        self._parent.update()

################################################################################
    async def set_name(self, interaction: Interaction) -> None:

        modal = SetNameModal(self.name)

        await interaction.response.send_modal(modal)
        await modal.wait()

        if not modal.complete:
            return

        self._name = modal.value
        self.update()

################################################################################
    async def set_age(self, interaction: Interaction) -> None:

        modal = SetAgeModal(self.age)

        await interaction.response.send_modal(modal)
        await modal.wait()

        if not modal.complete:
            return

        self._age = modal.value
        self.update()

################################################################################
    async def set_timezone(self, interaction: Interaction) -> None:

        prompt = ApplicationMessageManager.set_timezone(self.timezone)
        view = SetTimezoneView(interaction.user)

        await interaction.response.send_message(embed=prompt, view=view)
        await view.wait()

        if not view.complete or view.value is False:
            return

        self._timezone = view.value
        self.update()

################################################################################
    async def set_pronouns(self, interaction: Interaction) -> None:

        prompt = ApplicationMessageManager.set_pronouns(self.pronouns)
        view = SetPronounsView(interaction.user)

        await interaction.response.send_message(embed=prompt, view=view)
        await view.wait()

        if not view.complete or view.value is False:
            return

        self._pronouns = view.value
        self.update()

################################################################################
    async def set_languages(self, interaction: Interaction) -> None:

        prompt = ApplicationMessageManager.set_languages(self.languages)
        view = SetLanguagesView(interaction.user)

        await interaction.response.send_message(embed=prompt, view=view)
        await view.wait()

        if not view.complete or view.value is False:
            return

        self._languages = view.value
        self.update()

################################################################################
    async def set_dcworld(self, interaction: Interaction) -> None:

        prompt = ApplicationMessageManager.set_dcworld(self.datacenter, self.world)
        view = SetDCWorldView(interaction.user)

        await interaction.response.send_message(embed=prompt, view=view)
        await view.wait()

        if not view.complete or view.value is False:
            return

        self._datacenter = view.value[0]
        self._world = view.value[1]
        self.update()

################################################################################
    async def set_about(self, interaction: Interaction) -> None:

        modal = SetAboutMeModal(self.about)

        await interaction.response.send_modal(modal)
        await modal.wait()

        if not modal.complete:
            return

        self._about = modal.value
        self.update()

################################################################################
    async def set_notes(self, interaction: Interaction) -> None:

        modal = SetNotesModal(self.notes)

        await interaction.response.send_modal(modal)
        await modal.wait()

        if not modal.complete:
            return

        self._notes = modal.value
        self.update()

################################################################################
