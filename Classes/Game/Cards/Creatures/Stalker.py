from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("StalkerCard",)

################################################################################
class StalkerCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.Stalker,
            name="Stalker",
            description=(
                "The Stalker is a curious and sometimes aggressive creature that "
                "inhabits the kelp forests. It's known to collect metal debris, "
                "and while it can pose a threat, it may also lead players to valuable resources."
            ),
            effect=None,
            image=None,  # type: ignore
        )

################################################################################
