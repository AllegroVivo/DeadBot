from __future__ import annotations

from Classes.Game.Equipment import EquipmentCard
from Utils import EquipmentType
################################################################################

__all__ = ("SeaglideCard",)

################################################################################
class SeaglideCard(EquipmentCard):

    def __init__(self):

        super().__init__(
            _type=EquipmentType.Seaglide,
            name="Seaglide",
            description=(
                "The Seaglide is a personal transportation device used for "
                "faster underwater navigation. It's equipped with a small "
                "electric motor that propels the user through the water, "
                "allowing for swift exploration and escape from potential threats."
            ),
            effect=None,
            image=None,  # type: ignore
        )

################################################################################
