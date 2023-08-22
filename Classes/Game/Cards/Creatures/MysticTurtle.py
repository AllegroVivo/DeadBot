from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("MysticTurtleCard",)

################################################################################
class MysticTurtleCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.MysticTurtle,
            name="Mystic Turtle",
            effect="Look at the top 3 cards of any draw pile and rearrange them.",
            description=(
                "An ancient turtle with wisdom and foresight."
            ),
            image=None,  # type: ignore
        )

################################################################################
