from __future__ import annotations

from typing import TYPE_CHECKING, List, Any, Dict, TypeVar, Type

from discord import Interaction

if TYPE_CHECKING:
    from Classes import DeadBot, Application, GuildData
################################################################################

__all__ = ("ApplicationManager",)

AM = TypeVar("AM", bound="ApplicationManager")

################################################################################
class ApplicationManager:

    __slots__ = (
        "_state",
        "_applications",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, parent: GuildData, **kwargs):

        self._state: GuildData = parent
        self._applications: List[Application] = kwargs.pop("apps", None) or []

################################################################################
    @classmethod
    async def load_from_data(cls: Type[AM], parent: GuildData, data: Dict[str, Any]) -> AM:

        self: AM = cls.__new__(cls)

        apps = []
        for app_id, record in data.items():
            user = await parent.bot.get_or_fetch_user(record[2])
            if user is None:
                continue
            apps.append(Application.load(self.parent, user, app_id, record))

        self._state = parent
        self._applications = apps

        return self

################################################################################
    @property
    def bot(self) -> DeadBot:

        return self._state.bot

################################################################################
    def add_application(self, interaction: Interaction) -> Application:

        application = Application.new(self, interaction.user)
        self._applications.append(application)

        return application

################################################################################
    def update(self, instance: Application, exp_updated: bool) -> None:

        self.bot.database.update.application(instance, exp_updated)

################################################################################
