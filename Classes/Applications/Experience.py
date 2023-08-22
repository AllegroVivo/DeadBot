from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional, Any, Dict, Type, TypeVar
from uuid import UUID

from discord import Interaction

from Classes.Applications import ApplicationMessageManager
from Utils import *

if TYPE_CHECKING:
    from Classes import DeadBot, Application
################################################################################

__all__ = ("ApplicationExperience", "PriorWorkExp")

AE = TypeVar("AE", bound="ApplicationExperience")

################################################################################
@dataclass
class PriorWorkExp:

    id: UUID
    position: str
    venue: str
    time: str

################################################################################
class ApplicationExperience:

    __slots__ = (
        "_parent",
        "_work_exp",
        "_choice",
        "_level",
        "_nsfw",
        "_sample",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, parent: Application, **kwargs):

        self._parent: Application = parent

        self._work_exp: List[PriorWorkExp] = kwargs.pop("exp_list", None) or []

        self._choice: bool = kwargs.pop("choice", False)
        self._level: RPLevel = kwargs.pop("level", RPLevel.Null)
        self._nsfw: bool = kwargs.pop("nsfw", False)
        self._sample: Optional[str] = kwargs.pop("sample", None)

################################################################################
    @classmethod
    def load(cls: Type[AE], parent: Application, record: Dict[str, Any]) -> AE:

        main = record["Main"]

        return cls(
            parent=parent,
            exp_list=[
                PriorWorkExp(
                    id=UUID(exp[0]),
                    position=exp[2],
                    venue=exp[3],
                    time=exp[4]
                ) for exp in record["Exp"]
            ],
            choice=main[-1],
            level=RPLevel(main[-2]),
            nsfw=main[-3],
            sample=main[-4]
        )

################################################################################
    @property
    def work_experience(self) -> List[PriorWorkExp]:

        return self._work_exp

################################################################################
    @property
    def rp_choice(self) -> bool:

        return self._choice

################################################################################
    @property
    def rp_level(self) -> RPLevel:

        return self._level

################################################################################
    @property
    def rp_nsfw(self) -> bool:

        return self._nsfw

################################################################################
    @property
    def rp_sample(self) -> Optional[str]:

        return self._sample

################################################################################
    def set_work_experience(self, interaction: Interaction) -> None:

        prompt = ApplicationMessageManager.set_work_exp()

################################################################################
