from __future__ import annotations

import pygame
from discord import Bot
from typing import TYPE_CHECKING, List, Any, Tuple, Dict, Union

from .System import Database, GuildManager

if TYPE_CHECKING:
    from discord import Attachment, Guild
    from .System import GuildData
################################################################################

__all__ = ("DeadBot",)

################################################################################
class DeadBot(Bot):

    __slots__ = (
        "_database",
        "_fguilds",
        "_image_dump",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self._database: Database = Database(self)
        self._fguilds: GuildManager = GuildManager(self)

        self._image_dump: TextChannel = None  # type: ignore

        # Initialize pygame so we can render player hands on the fly.
        # pygame.init()

################################################################################
    async def load_all(self) -> None:

        # Initialize components
        self._database.build_all()

        self._fguilds.load_guilds()

        print("Fetching image dump...")
        self._image_dump = await self.fetch_channel(991902526188302427)

        # Get database payload
        print("Querying database...")
        payload = self.database.load_all()

        print("Parsing...")
        # Separate payload into individual lists
        positions = payload["positions"]
        applications = payload["applications"]

        # Create a dictionary to hold parsed data - guild_id is the main key for each entry
        data_dict: Dict[int, Dict[str, Any]] = {
            g.id: {
                "Positions": [],
                "Applications": {}
            } for g in self.guilds
        }

        # Parse Positions data
        for p in positions:
            try:
                data_dict[p[1]]["Positions"].append(p)
            except KeyError:  # This means we have data on a guild that we're no longer in. Just skip it.
                continue

        # Parse Applications data - a little more involved...
        apps_main = applications["main"]
        apps_exp = applications["exp"]
        for a in apps_main:
            try:
                data_dict[a[1]]["Applications"][a[0]] = {
                    "Main": a,
                    "Exp": []
                }
            except KeyError:
                continue
        for exp in apps_exp:
            try:
                data_dict[exp[1]]["Applications"][exp[0]]["Exp"].append(exp)
            except KeyError:
                continue

        print("Loading...")
        # Drop into guilds
        for g in self.fguilds:
            print(f"ID: {g.guild_id:>19} | Guild: {g.parent.name}")
            await g.load_all(self, g, data_dict[g.guild_id])

        print("Done!")

################################################################################
##### INTERNAL METHODS #########################################################
################################################################################
    def __getitem__(self, guild_id: int) -> GuildData:

        return self._fguilds[guild_id]

################################################################################
##### PROPERTIES ###############################################################
################################################################################
    @property
    def fguilds(self) -> List[GuildData]:

        return self._fguilds._guilds

################################################################################
    @property
    def database(self) -> Database:

        return self._database

################################################################################
##### PUBLIC METHODS ###########################################################
################################################################################
    async def dump_image(self, image: Attachment) -> str:

        file = await image.to_file()
        post = await self._image_dump.send(file=file)

        return post.attachments[0].url

################################################################################
    def get_fguild(self, guild: Guild) -> GuildData:

        return self._fguilds.get_guild(guild)

################################################################################
