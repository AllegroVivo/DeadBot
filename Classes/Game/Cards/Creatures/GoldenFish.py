from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("GoldenFishCard",)

################################################################################
class GoldenFishCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.GoldenFish,
            name="Golden Fish",
            effect="Gain an extra action on your next turn.",
            description=(
                "A rare fish that grants wishes to those lucky enough to encounter it."
            ),
            image=None,  # type: ignore
        )

################################################################################
