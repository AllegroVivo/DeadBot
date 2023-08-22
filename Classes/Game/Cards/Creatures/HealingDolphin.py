from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("HealingDolphinCard",)

################################################################################
class HealingDolphinCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.HealingDolphin,
            name="Healing Dolphin",
            effect="Recover a discarded Equipment Card.",
            description=(
                "A playful dolphin known for its healing abilities."
            ),
            image=None,  # type: ignore
        )

################################################################################
