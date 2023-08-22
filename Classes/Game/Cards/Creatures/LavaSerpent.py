from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("LavaSerpentCard",)

################################################################################
class LavaSerpentCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.LavaSerpent,
            name="Lava Serpent",
            effect="Destroy a player's Equipment Card.",
            description=(
                "A fiery serpent that dwells near underwater volcanoes."
            ),
            image=None,  # type: ignore
        )

################################################################################
