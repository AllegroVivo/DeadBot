from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("ElectricEelCard",)

################################################################################
class ElectricEelCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.ElectricEel,
            name="Electric Eel",
            effect="Shock a player, causing them to discard an Equipment Card or lose a turn.",
            description=(
                "A slippery eel capable of generating powerful electric shocks."
            ),
            image=None,  # type: ignore
        )

################################################################################
