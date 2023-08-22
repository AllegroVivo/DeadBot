from __future__ import annotations

from Classes.Game.Creature import CreatureCard
from Utils import CreatureType
################################################################################

__all__ = ("AbyssalKrakenCard",)

################################################################################
class AbyssalKrakenCard(CreatureCard):

    def __init__(self):

        super().__init__(
            _type=CreatureType.AbyssalKraken,
            name="Abyssal Kraken",
            effect="Grasp a player, causing them to lose two turns or discard two Equipment Cards.",
            description=(
                "A legendary creature lurking in the abyss, known for its massive "
                "tentacles and fearsome strength."
            ),
            image=None,  # type: ignore
        )

################################################################################
