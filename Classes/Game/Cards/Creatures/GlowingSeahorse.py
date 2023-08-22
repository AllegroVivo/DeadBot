from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("GlowingSeahorseCard",)

################################################################################
class GlowingSeahorseCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.GlowingSeahorse,
            name="Glowing Seahorse",
            effect="Draw 2 Resource Cards.",
            description=(
                "A magical seahorse that guides explorers to hidden treasures."
            ),
            image=None,  # type: ignore
        )

################################################################################
