from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("FrostbiteSharkCard",)

################################################################################
class FrostbiteSharkCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.FrostbiteShark,
            name="Frostbite Shark",
            effect="Attack a player, causing them to discard 2 Resource Cards.",
            description=(
                "A fearsome shark with razor-sharp teeth that thrives in icy waters."
            ),
            image=None,  # type: ignore
        )

################################################################################
