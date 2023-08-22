from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from .Card import SubnauticaCard
from Utils import CreatureType

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("CreatureCard",)

################################################################################
class CreatureCard(SubnauticaCard):

    def __init__(
        self,
        _type: CreatureType,
        name: str,
        description: str,
        effect: Optional[str],
        image: str,
    ):
        super().__init__(_type, name, description, effect, image)

################################################################################
    @property
    def card_type(self) -> CreatureType:

        return self._type

################################################################################
