from __future__ import annotations

from Classes.Game.Resource import ResourceCard
from Utils import ResourceType
################################################################################

__all__ = ("FishCard",)

################################################################################
class FishCard(ResourceCard):

    def __init__(self):

        super().__init__(
            _type=ResourceType.Fish,
            name="Fish",
            description=(
                "Fish are a primary source of sustenance and hydration in the "
                "ocean. They can be caught and cooked for nourishment or used "
                "in crafting unique underwater equipment."
            ),
            effect=None,
            image=None,  # type: ignore
            value=1
        )

################################################################################
