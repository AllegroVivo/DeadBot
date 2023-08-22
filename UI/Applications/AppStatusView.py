from __future__ import annotations

from discord import ButtonStyle, InputTextStyle, Interaction, User
from discord.ui import Select, Button
from typing import TYPE_CHECKING, Any, List, Optional, Tuple

from UI import SetStyleButton
from UI.Modal import FroggeModal
from UI.View import FroggeView
from Utils import *

if TYPE_CHECKING:
    from Classes import Application
################################################################################

__all__ = ("ApplicationStatusView",)

################################################################################
class ApplicationStatusView(FroggeView):

    def __init__(self, owner: User, application: Application):

        super().__init__(owner=owner)

        self.application: Application = application

        component_list = [

        ]

        for item in component_list:
            self.add_item(item)

################################################################################
class EditNameButton(SetStyleButton):

    def __init__(self, name: Optional[str]):
        super().__init__(
            label="Name",
            disabled=False,
            row=0,
        )

        self.set_style(name)

    async def callback(self, interaction: Interaction):
        await self.view.application.set_name(interaction)

################################################################################
class EditAgeButton(SetStyleButton):

    def __init__(self, age: Optional[str]):
        super().__init__(
            label="Age",
            disabled=False,
            row=0,
        )

        self.set_style(age)

    async def callback(self, interaction: Interaction):
        await self.view.application.set_age(interaction)

################################################################################
class EditPronounsButton(SetStyleButton):

    def __init__(self, pronouns: List[Pronoun]):
        super().__init__(
            label="Pronouns",
            disabled=False,
            row=0,
        )

        self.set_style(pronouns)

    async def callback(self, interaction: Interaction):
        await self.view.application.set_pronouns(interaction)

################################################################################
class EditTimezoneButton(SetStyleButton):

    def __init__(self, timezone: Optional[TimeZone]):
        super().__init__(
            label="Timezone",
            disabled=False,
            row=0,
        )

        self.set_style(timezone)

    async def callback(self, interaction: Interaction):
        await self.view.application.set_timezone(interaction)

################################################################################
class EditLanguagesButton(SetStyleButton):

    def __init__(self, languages: List[Language]):
        super().__init__(
            label="Languages",
            disabled=False,
            row=0,
        )

        self.set_style(languages)

    async def callback(self, interaction: Interaction):
        await self.view.application.set_languages(interaction)

################################################################################
class EditDCWorldButton(SetStyleButton):

    def __init__(self, dc: DataCenter):
        super().__init__(
            label="Data Center/Home World",
            disabled=False,
            row=1,
        )

        self.set_style(dc)

    async def callback(self, interaction: Interaction):
        await self.view.application.set_dcworld(interaction)

################################################################################
class EditAboutButton(SetStyleButton):

    def __init__(self, about: Optional[str]):
        super().__init__(
            label="About Me / Bio",
            disabled=False,
            row=1,
        )

        self.set_style(about)

    async def callback(self, interaction: Interaction):
        await self.view.application.set_about(interaction)

################################################################################
class EditNotesButton(SetStyleButton):

    def __init__(self, notes: Optional[str]):
        super().__init__(
            label="Additional Notes",
            disabled=False,
            row=1,
        )

        self.set_style(notes)

    async def callback(self, interaction: Interaction):
        await self.view.application.set_notes(interaction)

################################################################################
class EditWorkExpButton(Button):

    def __init__(self, work_exp: Optional[str]):
        super().__init__(
            style=ButtonStyle.blurple,
            label="I have Previous Work Experience to Report!",
            disabled=False,
            row=2,
        )

    async def callback(self, interaction: Interaction):
        await self.view.application.set_work_exp(interaction)

################################################################################
