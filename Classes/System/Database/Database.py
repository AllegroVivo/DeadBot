from __future__ import annotations

import os
import psycopg2

from dotenv import load_dotenv
from typing import TYPE_CHECKING, Any, Dict, Tuple, Union

from .Worker import DatabaseWorker

if TYPE_CHECKING:
    from psycopg2.extensions import connection, cursor

    from .Inserter import DatabaseInserter
    from .Updater import DatabaseUpdater
    from .Deleter import DatabaseDeleter
    from Classes import DeadBot
################################################################################

__all__ = ("Database", )

################################################################################
class Database:

    __slots__ = (
        "_state",
        "__connection",
        "_cursor",
        "_worker",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, bot: DeadBot):

        self._state: DeadBot = bot

        self.__connection: connection = None  # type: ignore
        self._connect()

        self._cursor: cursor = None  # type: ignore
        self._worker: DatabaseWorker = DatabaseWorker(bot)

################################################################################
    def _connect(self) -> None:

        # Look at me being fancy with an assert statement.
        assert self.__connection is None, "Database connection already exists!"

        print("Connecting to Database...")

        load_dotenv()
        self.__connection = psycopg2.connect(
            os.getenv("DATABASE_URL"), sslmode="require"
        )

        print("Connected successfully!")

################################################################################
##### INTERNAL METHODS #########################################################
################################################################################
    def __enter__(self) -> cursor:

        self._get_cursor()
        return self._cursor

################################################################################
    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:

        self._commit()
        self._close_cursor()

################################################################################
    def _commit(self) -> None:

        self.__connection.commit()

################################################################################
    def _get_cursor(self) -> None:

        self._cursor = self.__connection.cursor()

################################################################################
    def _close_cursor(self) -> None:

        self._cursor.close()

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def connection(self) -> connection:

        return self.__connection

################################################################################
    @property
    def cursor(self) -> None:

        raise Exception("Cursor is not a property of Database. Use __enter__ instead.")

################################################################################
    @property
    def insert(self) -> DatabaseInserter:

        return self._worker._inserter

################################################################################
    @property
    def update(self) -> DatabaseUpdater:

        return self._worker._updater

################################################################################

    @property
    def delete(self) -> DatabaseDeleter:

        return self._worker._deleter

################################################################################
##### PUBLIC METHODS ###########################################################
################################################################################
    def build_all(self) -> None:

        self._worker.build_all()

################################################################################
    def load_all(self) -> Dict[str, Any]:

        return self._worker.load_all()

################################################################################
