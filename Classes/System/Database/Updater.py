from __future__ import annotations

from typing import TYPE_CHECKING

from .Branch import DBWorkerBranch

if TYPE_CHECKING:
    from Classes import Position, Application
################################################################################

__all__ = ("DatabaseUpdater",)

################################################################################
class DatabaseUpdater(DBWorkerBranch):

    def update_position(self, position: Position) -> None:

        with self.database as db:
            db.execute(
                "UPDATE Positions "
                "SET name = %s, description = %s, salary = %s, enabled = %s "
                "WHERE _id = %s",
                (
                    position.name, position.description, position.salary,
                    position.enabled, position.id
                )
            )

################################################################################
    def update_application(self, app: Application, exp_updated: bool) -> None:

        with self.database as db:
            db.execute(
                "UPDATE Applications "
                "SET positions = %s, name = %s, age = %s, timezone = %s, "
                "pronouns = %s, languages = %s, datacenter = %s, world = %s, "
                "about = %s, image = %s, notes = %s, approved = %s "
                "WHERE _id = %s",
                (
                    [p.id for p in app.positions], app.name, app.age, app.timezone,
                    [p.value for p in app.pronouns], [l.value for l in app.languages],
                    app.datacenter.value, app.world.value, app.about, app.image,
                    app.notes, app.approved, app.id
                )
            )
            if exp_updated:
                db.execute(
                    "UPDATE rp_experience "
                    "SET choice = %s, level = %s, nsfw = %s, sample = %s "
                    "WHERE app_id = %s",
                    (
                        app.rp_choice, app.rp_level.value, app.rp_nsfw,
                        app.rp_sample, app.id
                    )
                )

################################################################################
    # Class Aliases

    position = update_position
    application = update_application

################################################################################
