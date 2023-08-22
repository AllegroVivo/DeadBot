from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from .Branch import DBWorkerBranch

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("DatabaseDeleter",)

################################################################################
class DatabaseDeleter(DBWorkerBranch):

    def delete_work_experience(self, exp_id: UUID) -> None:

        with self.database as db:
            db.execute(
                "DELETE FROM work_experience WHERE _id = %s",
                (str(exp_id),)
            )

################################################################################
    # Class Aliases

    work_exp = delete_work_experience

################################################################################
