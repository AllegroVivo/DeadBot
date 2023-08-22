from __future__ import annotations

from typing import TYPE_CHECKING, Union, List, Optional

from .PlayerHand import SubnauticaPlayerHand
from .PlayerStats import SubnauticaPlayerStats

if TYPE_CHECKING:
    from discord import User, Message

    from Classes import SubnauticaGame, ResourceCard, CreatureCard, EquipmentCard
    from UI import ActivePlayerView, InactivePlayerView
################################################################################

__all__ = ("SubnauticaPlayer",)

################################################################################
class SubnauticaPlayer:

    __slots__ = (
        "_user",
        "_current",
        "_stats",
        "_hand",
    )

################################################################################
    def __init__(self, user: User):

        self._user: User = user

        self._current: Optional[SubnauticaGame] = None

        self._stats: SubnauticaPlayerStats = SubnauticaPlayerStats(self)
        self._hand: SubnauticaPlayerHand = SubnauticaPlayerHand(self)

################################################################################
    def __eq__(self, other: SubnauticaPlayer) -> bool:

        return self.user.id == other.user.id

################################################################################
    @property
    def user(self) -> User:

        return self._user

################################################################################
    @property
    def stats(self) -> SubnauticaPlayerStats:

        return self._stats

################################################################################
    @property
    def cards(self) -> List[ResourceCard]:

        return self._hand.resources + self._hand.creatures + self._hand.equipment

################################################################################
    @property
    def resources(self) -> List[ResourceCard]:

        return self._hand.resources

################################################################################
    @property
    def equipment(self) -> List[EquipmentCard]:

        return self._hand.equipment

################################################################################
    @property
    def is_active(self) -> bool:

        return self == self.game.current_player

################################################################################
    @property
    def hand(self) -> Optional[Message]:

        return self._hand.message

################################################################################
    @hand.setter
    def hand(self, message: Message) -> None:

        self._hand._hand_msg = message

################################################################################
    @property
    def view(self) -> Union[ActivePlayerView, InactivePlayerView]:

        return self._hand.view

################################################################################
    @view.setter
    def view(self, view: Union[ActivePlayerView, InactivePlayerView]) -> None:

        self._hand._hand_view = view

################################################################################
    def register(self, game: SubnauticaGame) -> None:

        self._current = game

################################################################################
