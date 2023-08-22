from __future__ import annotations

from Classes.Game.Equipment import EquipmentCard
from Utils import EquipmentType
################################################################################

__all__ = ("ScannerCard",)

################################################################################
class ScannerCard(EquipmentCard):

    def __init__(self):

        super().__init__(
            _type=EquipmentType.Scanner,
            name="Scanner",
            description=(
                "The Scanner is a handheld device that allows players to analyze "
                "and identify various resources, creatures, and anomalies within "
                "the ocean depths. By scanning objects, players can gain valuable "
                "information, unlock new crafting recipes, and uncover hidden "
                "secrets of the aquatic world."
            ),
            effect=None,
            image=None,  # type: ignore
        )

################################################################################
