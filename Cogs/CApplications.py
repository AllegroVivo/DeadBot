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

from Classes.Applications import ApplicationMessageManager

if TYPE_CHECKING:
    from Classes import DeadBot
################################################################################

__all__ = ("Applications",)

################################################################################
class Applications(Cog):

    def __init__(self, bot: "DeadBot"):

        self.bot: "DeadBot" = bot

################################################################################

    applications = SlashCommandGroup(
        name="apply",
        description="Commands for applying to a job position.",
    )

################################################################################
    @applications.command(
        name="new",
        description="Create a new employment application.",
    )
    async def positions_add(self, ctx: ApplicationContext) -> None:

        guild = self.bot[ctx.guild.id]
        application = guild.get_application(ctx.user)

        await application.resume(ctx.interaction)

################################################################################
def setup(bot: "DeadBot") -> None:

    bot.add_cog(Applications(bot))

################################################################################
