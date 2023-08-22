from discord import (
    ApplicationContext,
    Cog,
    Member,
    Option,
    SlashCommandGroup,
    SlashCommandOptionType,
    User
)
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from Classes import DeadBot
################################################################################

__all__ = ("Internal", )

################################################################################
class Internal(Cog):

    def __init__(self, bot: "DeadBot"):

        self.bot: "DeadBot" = bot

################################################################################
    @Cog.listener("on_ready")
    async def load_internals(self) -> None:

        print("Loading internals...")
        await self.bot.load_all()

################################################################################
def setup(bot: "DeadBot") -> None:

    bot.add_cog(Internal(bot))

################################################################################
