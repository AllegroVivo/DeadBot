from discord import SelectOption
from enum import Enum
from typing import List, Union, Type
################################################################################

__all__ = (
    "Pronoun",
    "DataCenter",
    "AetherWorld",
    "CrystalWorld",
    "DynamisWorld",
    "PrimalWorld",
    "ChaosWorld",
    "LightWorld",
    "MateriaWorld",
    "ManaWorld",
    "ElementalWorld",
    "GaiaWorld",
    "MeteorWorld",
    "WorldEnum",
    "RPLevel",
    "world_enum_factory",
    "get_world_enum",
    "PreviousPosition",
    "TimeZone",
    "Language",
)

################################################################################
class FroggeEnum(Enum):

    @classmethod
    def select_options(cls) -> List[SelectOption]:

        return [SelectOption(label=member.name, value=str(member.value)) for member in cls]

################################################################################
class WorldEnum(FroggeEnum):

    pass

################################################################################
class Pronoun(FroggeEnum):

    He = 1
    Him = 2
    His = 3
    She = 4
    Her = 5
    Hers = 6
    They = 7
    Them = 8
    Theirs = 9
    Ze = 10
    Hir = 11
    Per = 12
    Pers = 13
    It = 14
    Its = 15
    Other = 16

################################################################################
class DataCenter(FroggeEnum):

    Null = 0
    Aether = 1
    Chaos = 2
    Crystal = 3
    Dynamis = 4
    Elemental = 5
    Gaia = 6
    Light = 7
    Mana = 8
    Materia = 9
    Meteor = 10
    Oceanian = 11
    Primal = 12

################################################################################
class AetherWorld(WorldEnum):

    Null = 0
    Adamantoise = 1
    Cactuar = 2
    Faerie = 3
    Gilgamesh = 4
    Jenova = 5
    Midgardsormr = 6
    Sargatanas = 7
    Siren = 8

################################################################################
class CrystalWorld(WorldEnum):

    Balmung = 11
    Brynhildr = 12
    Coeurl = 13
    Diabolos = 14
    Goblin = 15
    Malboro = 16
    Mateus = 17
    Zalera = 18

################################################################################
class DynamisWorld(WorldEnum):

    Halicarnassus = 21
    Maduin = 22
    Marilith = 23
    Seraph = 24

################################################################################
class PrimalWorld(WorldEnum):

    Behemoth = 31
    Excalibur = 32
    Exodus = 33
    Famfrit = 34
    Hyperion = 35
    Lamia = 36
    Leviathan = 37
    Ultros = 38

################################################################################
class ChaosWorld(WorldEnum):

    Cerberus = 41
    Louisoix = 42
    Moogle = 43
    Omega = 44
    Phantom = 45
    Ragnarok = 46
    Sagittarius = 47
    Spriggan = 48

################################################################################
class LightWorld(WorldEnum):

    Alpha = 51
    Lich = 52
    Odin = 53
    Phoenix = 54
    Raiden = 55
    Shiva = 56
    Twintania = 57
    Zodiark = 58

################################################################################
class MateriaWorld(WorldEnum):

    Bismarck = 61
    Ravana = 62
    Sephirot = 63
    Sophia = 64
    Zurvan = 65

################################################################################
class ElementalWorld(WorldEnum):

    Aegis = 71
    Atomos = 72
    Carbuncle = 73
    Garuda = 74
    Gungnir = 75
    Kujata = 76
    Tonberry = 77
    Typhon = 78

################################################################################
class GaiaWorld(WorldEnum):

    Alexander = 81
    Bahamut = 82
    Durandal = 83
    Fenrir = 84
    Ifrit = 85
    Ridill = 86
    Tiamat = 87
    Ultima = 88

################################################################################
class ManaWorld(WorldEnum):

    Anima = 91
    Asura = 92
    Chocobo = 93
    Hades = 94
    Ixion = 95
    Masamune = 96
    Pandaemonium = 97
    Titan = 98

################################################################################
class MeteorWorld(WorldEnum):

    Belias = 101
    Mandragora = 102
    Ramuh = 103
    Shinryu = 104
    Unicorn = 105
    Valefor = 106
    Yojimbo = 107
    Zeromus = 108

################################################################################
WORLD_ENUMS = {
    DataCenter.Null: AetherWorld,
    DataCenter.Aether: AetherWorld,
    DataCenter.Crystal: CrystalWorld,
    DataCenter.Dynamis: DynamisWorld,
    DataCenter.Primal: PrimalWorld,
    DataCenter.Chaos: ChaosWorld,
    DataCenter.Light: LightWorld,
    DataCenter.Materia: MateriaWorld,
    DataCenter.Mana: ManaWorld,
    DataCenter.Elemental: ElementalWorld,
    DataCenter.Gaia: GaiaWorld,
    DataCenter.Meteor: MeteorWorld,
}
################################################################################
def get_world_enum(data_center: DataCenter) -> Type[WorldEnum]:

    try:
        return WORLD_ENUMS[data_center]
    except KeyError:
        raise ValueError(f"Invalid data center: {data_center}")

################################################################################
def world_enum_factory(value: int) -> WORLD_ENUMS:

    for world_enum in WORLD_ENUMS.values():
        try:
            return world_enum(value)
        except ValueError:
            continue
    raise ValueError(f"Invalid World enum value: {value}")

################################################################################
class RPLevel(Enum):

    Null = 0
    Novice = 1
    Beginner = 2
    Learner = 3
    Intermediate = 4
    Proficient = 5
    Skilled = 6
    Competent = 7
    Experienced = 8
    Advanced = 9
    Expert = 10
    
################################################################################
    @staticmethod
    def select_options() -> List[SelectOption]:

        return [
            SelectOption(
                label=option.name,
                value=str(option.value)
            ) for option in RPLevel
        ]

################################################################################
class PreviousPosition(FroggeEnum):

    AdRunner = 1
    Administration = 2
    Bard = 3
    Bartender = 4
    Courtesan = 5
    Dancer = 6
    DJ = 7
    FortuneTeller = 8
    Gambling = 9
    Greeter = 10
    Host = 11
    Manager = 12
    Owner = 13
    Photographer = 14
    Security = 15
    TarotReader = 16

################################################################################
class TimeZone(Enum):

    Null = 0
    UTC = 1
    EST = 2
    CST = 3
    MST = 4
    PST = 5
    Other = 6

    ################################################################################
    @property
    def proper_name(self) -> str:

        match self.value:
            case 0:
                return "Unknown"
            case 1:
                return "UTC"
            case 2:
                return "Eastern Standard Time"
            case 3:
                return "Central Standard Time"
            case 4:
                return "Mountain Standard Time"
            case 5:
                return "Pacific Standard Time"
            case 6:
                return "Other Time Zone"

    ################################################################################
    @staticmethod
    def select_options() -> List[SelectOption]:

        zone_names = [
            "UTC",
            "Eastern Standard Time",
            "Central Standard Time",
            "Mountain Standard Time",
            "Pacific Standard Time",
            "Other"
        ]

        return [
            SelectOption(label=zone_names[member.value - 1], value=str(member.value))
            for member in TimeZone if member.value != 0
        ]

################################################################################
class Language(Enum):

    Null = 0
    English = 1
    French = 2
    German = 3
    Japanese = 4
    Other = 5

################################################################################
    @staticmethod
    def select_options() -> List[SelectOption]:

        return [
            SelectOption(label=member.name, value=str(member.value))
            for member in Language if member.value != 0
        ]

################################################################################
