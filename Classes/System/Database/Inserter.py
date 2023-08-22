from __future__ import annotations

from typing import TYPE_CHECKING, Optional
from uuid import UUID, uuid4

from discord import User

from .Branch import DBWorkerBranch

if TYPE_CHECKING:
    from Classes import GuildData, PriorWorkExp
################################################################################

__all__ = ("DatabaseInserter",)

################################################################################
class DatabaseInserter(DBWorkerBranch):

    def insert_position(
        self,
        guild: GuildData,
        name: str,
        description: Optional[str],
        salary: int
    ) -> UUID:

        _id = uuid4()

        with self.database as db:
            db.execute(
                "INSERT INTO positions(_id, guild_id, name, description, salary) "
                "VALUES(%s, %s, %s, %s, %s)",
                (str(_id), guild.guild_id, name, description, salary)
            )

        return _id

################################################################################
    def insert_application(
        self,
        guild: GuildData,
        user: User
    ) -> UUID:

        _id = uuid4()

        with self.database as db:
            db.execute(
                "INSERT INTO applications(_id, guild_id, user_id) "
                "VALUES(%s, %s, %s)",
                (str(_id), guild.guild_id, user.id)
            )
            db.execute(
                "INSERT INTO rp_experience(app_id) VALUES(%s)",
                (str(_id),)
            )

        return _id

################################################################################
    def insert_work_experience(self, app_id: UUID, prior: PriorWorkExp) -> UUID:

        _id = uuid4()

        with self.database as db:
            db.execute(
                "INSERT INTO work_experience(_id, app_id, position, venue,"
                "time) VALUES(%s, %s, %s, %s, %s)",
                (
                    str(_id), str(app_id), prior.position, prior.venue, prior.time
                )
            )

        return _id

################################################################################
    # Class Aliases

    position = insert_position
    application = insert_application
    work_exp = insert_work_experience

################################################################################
