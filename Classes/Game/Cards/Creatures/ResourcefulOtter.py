from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("ResourcefulOtterCard",)

################################################################################
class ResourcefulOtterCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.ResourcefulOtter,
            name="Resourceful Otter",
            effect="Exchange a Resource Card with another player.",
            description=(
                "A clever otter that's always finding and trading resources."
            ),
            image=None,  # type: ignore
        )

################################################################################
