from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, List
from uuid import uuid4, UUID

if TYPE_CHECKING:
    from Classes import DeadBot, Application
################################################################################

__all__ = ("WorkExperience",)

################################################################################
@dataclass
class PriorWorkExp:

    id: UUID
    position: str
    venue: str
    time: str

################################################################################
class WorkExperience:

    __slots__ = (
        "_parent",
        "_experience",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, parent: Application, exp_list: List[PriorWorkExp] = None):

        self._parent: Application = parent
        self._experience: List[PriorWorkExp] = exp_list or []

################################################################################
    @classmethod
    def new(cls, parent):

        pass

################################################################################
##### INTERNAL METHODS #########################################################
################################################################################

################################################################################
##### PROPERTIES ###############################################################
################################################################################

################################################################################
##### PUBLIC METHODS ###########################################################
################################################################################
