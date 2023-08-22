from __future__ import annotations
from .Branch import DBWorkerBranch
################################################################################

__all__ = ("DatabaseBuilder",)

################################################################################
class DatabaseBuilder(DBWorkerBranch):

    def assert_guild_records(self) -> None:

        pass

################################################################################
    def build_all(self) -> None:

        self.build_positions()
        self.build_applications()

################################################################################
    def build_positions(self) -> None:

        with self.database as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS positions ("
                "_id UUID PRIMARY KEY,"
                "guild_id BIGINT,"
                "name TEXT,"
                "description TEXT,"
                "salary INTEGER,"
                "enabled BOOLEAN DEFAULT TRUE"
                ")"
            )

################################################################################
    def build_applications(self) -> None:

        with self.database as db:
            db.execute(
                "CREATE TABLE IF NOT EXISTS applications ("
                "_id UUID PRIMARY KEY,"
                "guild_id BIGINT,"
                "user_id BIGINT,"
                "positions TEXT[],"
                "name TEXT,"
                "age TEXT,"
                "timezone INTEGER,"
                "pronouns INTEGER[],"
                "languages INTEGER[],"
                "datacenter INTEGER,"
                "world INTEGER,"
                "about TEXT,"
                "image TEXT,"
                "notes TEXT,"
                "approved BOOLEAN DEFAULT FALSE"
                ")"
            )
            db.execute(
                "CREATE TABLE IF NOT EXISTS work_experience ("
                "_id UUID PRIMARY KEY,"
                "app_id UUID,"
                "position TEXT,"
                "venue TEXT,"
                "time TEXT"
                ")"
            )
            db.execute(
                "CREATE TABLE IF NOT EXISTS rp_experience ("
                "app_id UUID PRIMARY KEY,"
                "choice BOOLEAN DEFAULT FALSE,"
                "level INTEGER,"
                "nsfw BOOLEAN DEFAULT FALSE,"
                "sample TEXT"
                ")"
            )

            db.execute(
                "CREATE OR REPLACE VIEW application_view AS "
                "SELECT "
                
                "apps._id,"
                "apps.guild_id,"
                "apps.user_id,"
                "apps.positions,"
                "apps.name,"
                "apps.age,"
                "apps.timezone,"
                "apps.pronouns,"
                "apps.languages,"
                "apps.datacenter,"
                "apps.world,"
                "apps.about,"
                "apps.image,"
                "apps.notes,"
                "apps.approved,"
                
                "rp.choice,"
                "rp.level,"
                "rp.nsfw,"
                "rp.sample "
                
                "FROM applications AS apps "
                "LEFT JOIN rp_experience AS rp ON apps._id = rp.app_id;"
            )

################################################################################
