from __future__ import annotations

from Classes.Game.Resource import ResourceCard
from Utils import ResourceType
################################################################################

__all__ = ("MetalCard",)

################################################################################
class MetalCard(ResourceCard):

    def __init__(self):

        super().__init__(
            _type=ResourceType.Metal,
            name="Metal",
            description=(
                "Metal is a versatile and sturdy material found in various "
                "parts of the ocean floor. It's essential for crafting basic "
                "tools, building structures, and reinforcing equipment."
            ),
            effect=None,
            image=None,  # type: ignore
            value=1
        )

################################################################################
