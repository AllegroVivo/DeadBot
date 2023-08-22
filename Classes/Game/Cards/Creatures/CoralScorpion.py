from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("CoralScorpionCard",)

################################################################################
class CoralScorpionCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.CoralScorpion,
            name="Coral Scorpion",
            effect="Sting a player, causing them to discard a Resource Card or lose a turn.",
            description=(
                "A scorpion-like creature that blends with coral reefs, known "
                "for its venomous sting."
            ),
            image=None,  # type: ignore
        )

################################################################################
