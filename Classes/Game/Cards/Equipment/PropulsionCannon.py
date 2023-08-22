from __future__ import annotations

from Classes.Game.Equipment import EquipmentCard
from Utils import EquipmentType
################################################################################

__all__ = ("PropulsionCannonCard",)

################################################################################
class PropulsionCannonCard(EquipmentCard):

    def __init__(self):

        super().__init__(
            _type=EquipmentType.PropulsionCannon,
            name="Propulsion Cannon",
            description=(
                "The Propulsion Cannon is a versatile tool that can move "
                "objects and fend off creatures. It uses advanced technology "
                "to generate a force field that can grab, hold, and launch "
                "various items, adding a new dimension to underwater "
                "manipulation and defense."
            ),
            effect=None,
            image=None,  # type: ignore
        )

################################################################################
