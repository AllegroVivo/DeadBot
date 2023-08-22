from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("GasopodCard",)

################################################################################
class GasopodCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.Gasopod,
            name="Gasopod",
            description=(
                "The Gasopod is a large, gentle creature known for the toxic gas "
                "it releases when threatened. While not directly aggressive, its "
                "defensive mechanisms can pose a hazard to unwary explorers."
            ),
            effect=None,
            image=None,  # type: ignore
        )

################################################################################
