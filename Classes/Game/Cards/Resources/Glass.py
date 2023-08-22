from __future__ import annotations

from Classes.Game.Resource import ResourceCard
from Utils import ResourceType
################################################################################

__all__ = ("GlassCard",)

################################################################################
class GlassCard(ResourceCard):

    def __init__(self):

        super().__init__(
            _type=ResourceType.Glass,
            name="Glass",
            description=(
                "Glass is a transparent and smooth material used for crafting "
                "optical equipment and waterproof structures. It's vital for "
                "creating items like the Seaglide and Oxygen Tank."
            ),
            effect=None,
            image=None,  # type: ignore
            value=1
        )

################################################################################
