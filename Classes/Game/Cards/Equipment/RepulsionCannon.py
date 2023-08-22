from __future__ import annotations

from Classes.Game.Equipment import EquipmentCard
from Utils import EquipmentType
################################################################################

__all__ = ("RepulsionCannonCard",)

################################################################################
class RepulsionCannonCard(EquipmentCard):

    def __init__(self):

        super().__init__(
            _type=EquipmentType.RepulsionCannon,
            name="Repulsion Cannon",
            description=(
                "The Repulsion Cannon is a powerful device that emits a strong "
                "force field, repelling dangerous creatures and clearing obstacles. "
                "It's a vital tool for defense and can create safe pathways through "
                "treacherous underwater terrain."
            ),
            effect=None,
            image=None,  # type: ignore
        )

################################################################################
