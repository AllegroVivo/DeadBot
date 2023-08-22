from __future__ import annotations

from Classes.Game.Resource import ResourceCard
from Utils import ResourceType
################################################################################

__all__ = ("PlantCard",)

################################################################################
class PlantCard(ResourceCard):

    def __init__(self):

        super().__init__(
            _type=ResourceType.Plant,
            name="Plant",
            description=(
                "Plants are diverse and abundant in the ocean, providing "
                "essential materials for crafting medicines, food, and "
                "biofuels. They are a renewable resource for survival."
            ),
            effect=None,
            image=None,  # type: ignore
            value=1
        )

################################################################################
