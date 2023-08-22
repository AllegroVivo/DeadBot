from __future__ import annotations

from typing import TYPE_CHECKING, Optional, List, Union, Any

from discord import Message
from pygame import Surface

from UI.Game import ActivePlayerView, InactivePlayerView

if TYPE_CHECKING:
    from Classes import DeadBot, SubnauticaPlayer, ResourceCard, EquipmentCard, CreatureCard
################################################################################

__all__ = ("SubnauticaPlayerHand",)

################################################################################
class SubnauticaPlayerHand:

    __slots__ = (
        "_player",
        "_resources",
        "_equipment",
        "_creatures",
        "_hand_msg",
        "_hand_view",
        "_hand_renderer",
        "_resource_count",
    )

################################################################################
    def __init__(self, player: SubnauticaPlayer):

        self._player: SubnauticaPlayer = player

        self._resources: List[ResourceCard] = []
        self._equipment: List[EquipmentCard] = []
        self._creatures: List[CreatureCard] = []

        self._hand_msg: Optional[Message] = None
        self._hand_view: Optional[Union[ActivePlayerView, InactivePlayerView]] = None
        self._hand_renderer: PlayerHandRenderer = PlayerHandRenderer(self)

        self._resource_count: int = 0

################################################################################
    def __iadd__(self, other: Any) -> SubnauticaPlayerHand:

        if other.__class__.__name__ not in ("ResourceCard", "EquipmentCard", "CreatureCard",):
            raise TypeError(
                f"unsupported operand type(s) for +=: 'SubnauticaPlayerHand' "
                f"and '{other.__class__.__name__}'"
            )

        if other.__class__.__name__ == "ResourceCard":
            self.add_resource(other)
            self._resource_count += 1
        elif other.__class__.__name__ == "EquipmentCard":
            self.add_equipment(other)
        else:
            self.add_creature(other)

        return self

################################################################################
    def __isub__(self, other: Any) -> SubnauticaPlayerHand:

        if other.__class__.__name__ not in ("ResourceCard", "EquipmentCard",):
            raise TypeError(
                f"unsupported operand type(s) for +=: 'SubnauticaPlayerHand' "
                f"and '{other.__class__.__name__}'"
            )

        if other.__class__.__name__ == "ResourceCard":
            self.resources.remove(other)
        else:
            self.equipment.remove(other)

        return self

################################################################################
    @property
    def resources(self) -> List[ResourceCard]:

        return self._resources

################################################################################
    @property
    def equipment(self) -> List[EquipmentCard]:

        return self._equipment

################################################################################
    @property
    def creatures(self) -> List[CreatureCard]:

        return self._creatures

################################################################################
    @property
    def message(self) -> Optional[Message]:

        return self._hand_msg

################################################################################
    @property
    def view(self) -> Union[ActivePlayerView, InactivePlayerView]:

        return self._hand_view

################################################################################
    @property
    def image(self) -> Optional[str]:

        return self._hand_img

################################################################################
    def add_resource(self, card: ResourceCard) -> None:

        self.resources.append(card)

################################################################################
    def add_equipment(self, card: EquipmentCard) -> None:

        self.equipment.append(card)

################################################################################
    def add_creature(self, card: CreatureCard) -> None:

        self.creatures.append(card)

################################################################################
class PlayerHandRenderer:

    __slots__ = (
        "_parent",
        "_surface",
    )

################################################################################
    def __init__(self, parent: SubnauticaPlayerHand):

        self._parent: SubnauticaPlayerHand = parent
        self._surface: Surface = Surface((1024, 768))

################################################################################
    @property
    def bot(self) -> DeadBot:

        return self._parent._player.bot

################################################################################
    def render(self) -> None:

        pass

################################################################################
