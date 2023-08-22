from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("JellyrayCard",)

################################################################################
class JellyrayCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.Jellyray,
            name="Jellyray",
            description=(
                "The Jellyray is a beautiful and bioluminescent creature that "
                "gracefully glides through the water. It's non-aggressive and "
                "can lead players to hidden beauty and wonders within the "
                "ocean depths."
            ),
            effect=None,
            image=None,  # type: ignore
        )

################################################################################
