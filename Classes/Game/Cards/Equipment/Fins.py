from __future__ import annotations

from Classes.Game.Equipment import EquipmentCard
from Utils import EquipmentType
################################################################################

__all__ = ("FinsCard",)

################################################################################
class FinsCard(EquipmentCard):

    def __init__(self):

        super().__init__(
            _type=EquipmentType.Fins,
            name="Fins",
            description=(
                "Fins enhance the player's swimming speed and agility. They are "
                "crafted from flexible materials that allow for more efficient "
                "movement through the water, aiding in exploration and evasion "
                "of dangers."
            ),
            effect=None,
            image=None,  # type: ignore
        )

################################################################################
