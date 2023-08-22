from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Tuple, Union

from .Branch import DBWorkerBranch

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("DatabaseLoader",)

################################################################################
class DatabaseLoader(DBWorkerBranch):

    def load_all(self) -> Dict[str, Any]:

        return {
            "positions" : self.load_positions(),
            "applications" : {
                "main" : self.load_applications_main(),
                "exp" : self.load_applications_exp()
            },
        }

################################################################################
    def load_positions(self) -> Tuple[Tuple[Any, ...]]:

        with self.database as db:
            db.execute("SELECT * FROM positions")
            return db.fetchall()

################################################################################
    def load_applications_main(self) -> Tuple[Tuple[Any, ...]]:

        with self.database as db:
            db.execute("SELECT * FROM application_view")
            return db.fetchall()

################################################################################
    def load_applications_exp(self) -> Tuple[Tuple[Any, ...]]:

        with self.database as db:
            db.execute("SELECT * FROM work_experience")
            return db.fetchall()

################################################################################
