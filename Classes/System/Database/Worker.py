from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Tuple, Union

from .Builder import DatabaseBuilder
from .Deleter import DatabaseDeleter
from .Inserter import DatabaseInserter
from .Loader import DatabaseLoader
from .Updater import DatabaseUpdater

if TYPE_CHECKING:
    from Classes import DeadBot
################################################################################

__all__ = ("DatabaseWorker", )

################################################################################
class DatabaseWorker:

    __slots__ = (
        "_state",
        "_inserter",
        "_updater",
        "_deleter",
        "_builder",
        "_loader",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, bot: DeadBot):

        self._state: DeadBot = bot

        self._builder: DatabaseBuilder = DatabaseBuilder(bot)
        self._inserter: DatabaseInserter = DatabaseInserter(bot)
        self._updater: DatabaseUpdater = DatabaseUpdater(bot)
        self._deleter: DatabaseDeleter = DatabaseDeleter(bot)
        self._loader: DatabaseLoader = DatabaseLoader(bot)

################################################################################
##### PUBLIC METHODS ###########################################################
################################################################################
    def build_all(self) -> None:

        self._builder.build_all()

################################################################################
    def load_all(self) -> Dict[str, Any]:

        return self._loader.load_all()

################################################################################
