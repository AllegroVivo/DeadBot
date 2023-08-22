from __future__ import annotations

from Classes.Game.Resource import ResourceCard
from Utils import ResourceType
################################################################################

__all__ = ("CrystalCard",)

################################################################################
class CrystalCard(ResourceCard):

    def __init__(self):

        super().__init__(
            _type=ResourceType.Crystal,
            name="Crystal",
            description=(
                "Crystals are rare and valuable minerals found in the deeper "
                "parts of the ocean. They are used to craft advanced technology "
                "and provide energy for various underwater devices."
            ),
            effect=None,
            image=None,  # type: ignore
            value=1
        )

################################################################################
