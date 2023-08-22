from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("WarperCard",)

################################################################################
class WarperCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.Warper,
            name="Warper",
            description=(
                "The Warper is a mysterious and enigmatic creature with the ability "
                "to teleport itself and others. Encountering a Warper can lead to "
                "unexpected twists and turns in a player's journey, adding an element "
                "of unpredictability and excitement."
            ),
            effect=None,
            image=None,  # type: ignore
        )

################################################################################
