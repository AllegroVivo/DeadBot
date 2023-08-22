from __future__ import annotations

from typing import TYPE_CHECKING, Any, Tuple, List, Optional, Type, TypeVar, Dict, Union

from Classes.Applications import ApplicationManager
from Classes.Game.LobbyMgr import SubnauticaLobbyManager
from Classes.Positions import PositionManager

if TYPE_CHECKING:
    from discord import Guild, User
    from uuid import UUID

    from Classes import DeadBot, Position, Application
################################################################################

__all__ = ("GuildData",)

GD = TypeVar("GD", bound="GuildData")

################################################################################
class GuildData:

    __slots__ = (
        "_state",
        "_parent",
        "_positions",
        "_lobbies",
        "_applications",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, bot: DeadBot, parent: Guild, **kwargs):

        self._state: DeadBot = bot
        self._parent: Guild = parent

        self._positions: PositionManager = kwargs.pop("pos_mgr", None) or PositionManager(self)
        self._lobbies: SubnauticaLobbyManager = SubnauticaLobbyManager(self.bot)
        self._applications: ApplicationManager = (
                kwargs.pop("app_mgr", None) or ApplicationManager(self)
        )

################################################################################
    @classmethod
    async def load_all(cls: Type[GD], bot: DeadBot, parent: GuildData, data: Dict[str, Any]) -> GD:

        return cls(
            bot=bot,
            parent=parent,
            pos_mgr=PositionManager.load_from_data(parent, data["Positions"]),
            app_mgr=await ApplicationManager.load_from_data(parent, data["Applications"])
        )

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def bot(self) -> DeadBot:

        return self._state

################################################################################
    @property
    def parent(self) -> Guild:

        return self._parent

################################################################################
    @property
    def guild_id(self) -> int:

        return self._parent.id

################################################################################
    @property
    def position_manager(self) -> PositionManager:

        return self._positions

################################################################################
    @property
    def application_manager(self) -> ApplicationManager:

        return self._applications

################################################################################
    @property
    def positions(self) -> List[Position]:

        return self._positions._positions

################################################################################
    @property
    def applications(self) -> List[Application]:

        return self._applications._applications

################################################################################
    @property
    def lobby_manager(self) -> SubnauticaLobbyManager:

        return self._lobbies

################################################################################
##### METHODS ##################################################################
################################################################################
    def get_position(self, name: str) -> Optional[Position]:

        for pos in self.positions:
            if pos.name.lower() == name.lower():
                return pos

################################################################################
    def get_application(self, user: User) -> Application:

        for app in self.applications:
            if app.user.id == user.id:
                return app

        application = Application.new(self.application_manager, user)
        self.application_manager._applications.append(application)

        return application

################################################################################
