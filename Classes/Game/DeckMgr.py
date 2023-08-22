from __future__ import annotations

import random

from typing import TYPE_CHECKING, List, Type, Any

from Classes.Game.Cards import *

if TYPE_CHECKING:
    from Classes import ResourceCard, CreatureCard, EquipmentCard, SubnauticaGame
################################################################################

__all__ = ("DeckManager",)

################################################################################
# Might make these Dicts later if I want to represent <card:number_in_deck> in the future
_resource_cards = [
    CoralCard, FishCard, MetalCard, PlantCard, CrystalCard, GlassCard
]
_equipment_cards = [
    ScannerCard, SeaglideCard, OxygenTankCard, FinsCard, PropulsionCannonCard,
    RepulsionCannonCard
]
_creature_cards = [
    AbyssalKrakenCard,
    CoralScorpionCard,
    ElectricEelCard,
    FrostbiteSharkCard,
    GasopodCard,
    GlowingSeahorseCard,
    GoldenFishCard,
    HarmonyWhaleCard,
    HealingDolphinCard,
    JellyrayCard,
    LavaSerpentCard,
    MysticTurtleCard,
    PoisonousJellyCard,
    ReaperLeviathanCard,
    ResourcefulOtterCard,
    SandsharkCard,
    StalkerCard,
    WarperCard
]
################################################################################
class DeckManager:

    __slots__ = (
        "_parent",
        "_resources",
        "_equipment",
        "_creatures",
    )

    __RESOURCE_TYPES: List[Type[ResourceCard]] = [card for card in _resource_cards for _ in range(6)]
    __EQUIPMENT_TYPES: List[Type[EquipmentCard]] = [card for card in _equipment_cards for _ in range(4)]
    __CREATURE_TYPES: List[Type[CreatureCard]] = [card for card in _creature_cards]

################################################################################
    def __init__(self, parent: SubnauticaGame):

        self._parent: SubnauticaGame = parent

        self._resources: List[ResourceCard] = self.new_resource_deck()
        self._equipment: List[EquipmentCard] = self.new_equipment_deck()
        self._creatures: List[CreatureCard] = self.new_creature_deck()

################################################################################
    @staticmethod
    def new_resource_deck() -> List[ResourceCard]:

        return [card() for card in DeckManager.__RESOURCE_TYPES]  # type: ignore

################################################################################
    @staticmethod
    def new_equipment_deck() -> List[EquipmentCard]:

        # We don't need any arguments for the card constructor (hence the ignore)
        # because we've actually got an array of pre-made classes, not the
        # base class. That applies to all three decks.
        return [card() for card in DeckManager.__EQUIPMENT_TYPES]  # type: ignore

################################################################################
    @staticmethod
    def new_creature_deck() -> List[CreatureCard]:

        return [card() for card in DeckManager.__CREATURE_TYPES]  # type: ignore

################################################################################
    @property
    def resource_deck(self) -> List[ResourceCard]:

        return self._resources

################################################################################
    @property
    def equipment_deck(self) -> List[EquipmentCard]:

        return self._equipment

################################################################################
    @property
    def creature_deck(self) -> List[CreatureCard]:

        return self._creatures

################################################################################
    def shuffle(self) -> None:

        random.shuffle(self._resources)
        random.shuffle(self._equipment)
        random.shuffle(self._creatures)

################################################################################
    def deal(self) -> None:

        for player in self._parent.players:
            for _ in range(5):
                player.hand.append(self._resources.pop())

################################################################################
