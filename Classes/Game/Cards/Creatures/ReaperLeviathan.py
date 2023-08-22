from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("ReaperLeviathanCard",)

################################################################################
class ReaperLeviathanCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.ReaperLeviathan,
            name="Reaper Leviathan",
            description=(
                "The Reaper Leviathan is a terrifying and aggressive predator "
                "found in the deep ocean. Its powerful jaws and swift movements "
                "make it a formidable threat to players, capable of destroying "
                "equipment and causing serious harm."
            ),
            effect=None,
            image=None,  # type: ignore
        )

################################################################################
