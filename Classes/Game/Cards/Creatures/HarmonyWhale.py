from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("HarmonyWhaleCard",)

################################################################################
class HarmonyWhaleCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.HarmonyWhale,
            name="Harmony Whale",
            effect="Protect from the next Dangerous Creature's effect.",
            description=(
                "A gentle giant that brings peace and harmony to the ocean."
            ),
            image=None,  # type: ignore
        )

################################################################################
