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
    from Classes import DeadBot, PositionManager
################################################################################

__all__ = ("Positions", )

################################################################################
class Positions(Cog):

    def __init__(self, bot: "DeadBot"):

        self.bot: "DeadBot" = bot

################################################################################

    positions = SlashCommandGroup(
        name="jobs",
        description="Commands for managing staff job Positions.",
    )

################################################################################
    @positions.command(
        name="add",
        description="Add a new job position.",
    )
    async def positions_add(self, ctx: ApplicationContext) -> None:

        pm = self.bot[ctx.guild.id].position_manager
        await pm.add_position(ctx.interaction)

################################################################################
    @positions.command(
        name="edit",
        description="Edit a job position.",
    )
    async def positions_edit(self, ctx: ApplicationContext) -> None:

        pm = self.bot[ctx.guild.id].position_manager
        await pm.edit_position(ctx.interaction)

################################################################################
    @positions.command(
        name="toggle",
        description="Enable/Disable a job position.",
    )
    async def positions_disable(self, ctx: ApplicationContext) -> None:

        pm = self.bot[ctx.guild.id].position_manager
        await pm.toggle_position(ctx.interaction)

################################################################################
def setup(bot: "DeadBot") -> None:

    bot.add_cog(Positions(bot))

################################################################################
