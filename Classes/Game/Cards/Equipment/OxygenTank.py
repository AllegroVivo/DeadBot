from __future__ import annotations

from Classes.Game.Equipment import EquipmentCard
from Utils import EquipmentType
################################################################################

__all__ = ("OxygenTankCard",)

################################################################################
class OxygenTankCard(EquipmentCard):

    def __init__(self):

        super().__init__(
            _type=EquipmentType.OxygenTank,
            name="Oxygen Tank",
            description=(
                "The Oxygen Tank is an essential piece of equipment for extended "
                "underwater exploration. It increases the player's ability to "
                "stay underwater, providing more time to explore, gather resources, "
                "and interact with the aquatic environment."
            ),
            effect=None,
            image=None,  # type: ignore
        )

################################################################################
