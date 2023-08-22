from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("SandsharkCard",)

################################################################################
class SandsharkCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.Sandshark,
            name="Sandshark",
            description=(
                "The Sandshark is a unique creature that burrows into the sandy "
                "ocean floor, ambushing prey and players alike. Its sudden attacks "
                "can be startling and dangerous, requiring caution when "
                "navigating sandy areas."
            ),
            effect=None,
            image=None,  # type: ignore
        )

################################################################################
