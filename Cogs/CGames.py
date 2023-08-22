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

__all__ = ("SubnauticaShuffle",)

################################################################################
class SubnauticaShuffle(Cog):

    def __init__(self, bot: "DeadBot"):

        self.bot: "DeadBot" = bot

################################################################################

    positions = SlashCommandGroup(
        name="game",
        description="Commands for playing Subnautica Shuffle.",
    )

################################################################################
    @positions.command(
        name="new",
        description="Start a new game of Subnautica Shuffle.",
    )
    async def game_new(self, ctx: ApplicationContext) -> None:

        lm = self.bot[ctx.guild.id].lobby_manager
        await lm.new_game(ctx.interaction)

################################################################################
def setup(bot: "DeadBot") -> None:

    bot.add_cog(SubnauticaShuffle(bot))

################################################################################
