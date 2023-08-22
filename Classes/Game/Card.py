from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Union, Optional

from Utils import CreatureType, EquipmentType, ResourceType

if TYPE_CHECKING:
    from Classes import SubnauticaGame
################################################################################

__all__ = ("SubnauticaCard",)

CARDTYPE = Union[CreatureType, EquipmentType, ResourceType]

################################################################################
class SubnauticaCard(ABC):

    __slots__ = (
        "_state",
        "_type",
        "_id",
        "_name",
        "_description",
        "_effect",
        "_image",
    )

################################################################################
    def __init__(
        self,
        _type: CARDTYPE,
        name: str,
        description: str,
        effect: Optional[str],
        image: str,
    ):

        self._type: CARDTYPE = _type

        self._name: str = name
        self._description: str = description
        self._effect: Optional[str] = effect
        self._image: str = image

################################################################################
    @property
    def id(self) -> str:

        return self._type.value  # type: ignore

################################################################################
    @property
    def name(self) -> str:

        return self._name

################################################################################
    @property
    def description(self) -> str:

        return self._description

################################################################################
    @property
    def image(self) -> str:

        return self._image

################################################################################
    @property
    def game(self) -> SubnauticaGame:

        return self._state

################################################################################
    @property  # (Property needs to come first here)
    @abstractmethod
    def card_type(self) -> Union[CreatureType, EquipmentType, ResourceType]:

        return self._type

################################################################################
