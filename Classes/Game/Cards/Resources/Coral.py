from __future__ import annotations

from Classes.Game.Resource import ResourceCard
from Utils import ResourceType
################################################################################

__all__ = ("CoralCard",)

################################################################################
class CoralCard(ResourceCard):

    def __init__(self):

        super().__init__(
            _type=ResourceType.Coral,
            name="Coral",
            description=(
                "Coral is a unique and colorful underwater organism used in "
                "various crafting recipes. It's essential for creating water "
                "purification tablets and decorative elements."
            ),
            effect=None,
            image=None,  # type: ignore
            value=1
        )

################################################################################
