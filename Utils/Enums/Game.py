from enum import Enum
################################################################################

_all__ = (

    "ResourceType",
    "EquipmentType",
    "CreatureType"
    "Player",
    "LogAction",
)

################################################################################
class ResourceType(Enum):

    Metal   = "RES-MTL"
    Glass   = "RES-GLS"
    Coral   = "RES-CRL"
    Plant   = "RES-PLT"
    Fish    = "RES-FSH"
    Crystal = "RES-CRY"

################################################################################
class EquipmentType(Enum):

    Scanner          = "EQUIP-SCN"
    Seaglide         = "EQUIP-SGL"
    OxygenTank       = "EQUIP-OXT"
    Fins             = "EQUIP-FNS"
    PropulsionCannon = "EQUIP-PRC"
    RepulsionCannon  = "EQUIP-RPC"

################################################################################
class CreatureType(Enum):

    # Dangerous
    FrostbiteShark = "CRE-001"
    LavaSerpent = "CRE-002"
    PoisonousJellyfish = "CRE-003"
    ElectricEel = "CRE-004"
    AbyssalKraken = "CRE-005"
    CoralScorpion = "CRE-006"

    # Friendly
    GlowingSeahorse = "CRE-007"
    HealingDolphin = "CRE-008"
    MysticTurtle = "CRE-009"
    HarmonyWhale = "CRE-010"
    ResourcefulOtter = "CRE-011"
    GoldenFish = "CRE-012"

    # Others Provided by ChatGPT that I didn't want to throw away
    # I'll probably use these for something else (Constructors are made just in case)
    ReaperLeviathan = "CRE-013"
    Gasopod = "CRE-014"
    Stalker = "CRE-015"
    Warper = "CRE-016"
    Sandshark = "CRE-017"
    Jellyray = "CRE-018"

################################################################################
class Player(Enum):

    Player1 = 0
    Player2 = 1
    Player3 = 2
    Player4 = 3

################################################################################
class LogAction(Enum):

    GameStart = 1
    Null = 0
    DrawResource = 2
    # etc...

################################################################################
    @property
    def proper_name(self) -> str:

        match self.name:
            case 0:
                return "N/A"
            case 2:
                return "Draw Resource"
            case 1:
                return "Game Start"
            # etc...
            case _:
                return "N/A"

################################################################################
