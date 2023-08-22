from __future__ import annotations

from typing import TYPE_CHECKING, Optional, List

from .Card import SubnauticaCard
from Utils import EquipmentType

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("EquipmentCard",)

################################################################################
class EquipmentCard(SubnauticaCard):

    def __init__(
        self,
        _type: EquipmentType,
        name: str,
        description: str,
        effect: Optional[str],
        image: str,
    ):

        super().__init__(_type, name, description, effect, image)

################################################################################
    @property
    def card_type(self) -> EquipmentType:

        return self._type

################################################################################
    @staticmethod
    def new_deck() -> List[EquipmentCard]:

        pass

################################################################################
