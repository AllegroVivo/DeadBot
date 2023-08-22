from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("PoisonousJellyCard",)

################################################################################
class PoisonousJellyCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.PoisonousJellyfish,
            name="Poisonous Jellyfish",
            effect="Sting a player, causing them to lose a turn or discard a Resource Card.",
            description=(
                "A dangerous jellyfish with potent venom that can paralyze its prey."
            ),
            image=None,  # type: ignore
        )

################################################################################
