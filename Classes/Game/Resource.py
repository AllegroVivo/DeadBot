from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from .Card import SubnauticaCard
from Utils import ResourceType

if TYPE_CHECKING:
    from Classes import SubnauticaGame
################################################################################

__all__ = ("ResourceCard",)

################################################################################
class ResourceCard(SubnauticaCard):

    __slots__ = (
        "_value",
    )

################################################################################
    def __init__(
        self,
        _type: ResourceType,
        name: str,
        description: str,
        effect: Optional[str],
        image: str,
        value: int
    ):

        super().__init__(_type, name, description, effect, image)

        self._value: int = value

################################################################################
    @property
    def card_type(self) -> ResourceType:

        return self._type

################################################################################
