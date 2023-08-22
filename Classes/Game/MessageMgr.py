from __future__ import annotations

from discord import Embed, EmbedField
from typing import TYPE_CHECKING, List

from Classes.Game import GameLog
from Classes.Game.LogItem import SubnauticaLogItem
from Utils import Utilities as U

if TYPE_CHECKING:
    from Classes import SubnauticaPlayer, SubnauticaTurn
################################################################################

__all__ = ("GameMessageManager",)

################################################################################
class GameMessageManager:

    def __init__(self):
        pass

################################################################################
    @staticmethod
    def confirm_game_start(players: List[SubnauticaPlayer]) -> Embed:

        return U.make_embed(
            title="Confirm Game Start",
            description=(
                "Are you sure you want to start the game?\n"
                "This will start the game for all players in the lobby.\n"
                f"{U.draw_line(extra=25)}\n"
                "__**Current Players**__\n"
                "\n".join([f"{player.user.mention}" for player in players])
            ),
            fields=[
                EmbedField(
                    name="Note",
                    value="*(You must have at least two (2) players to start a game.)*",
                    inline=False
                )
            ],
            footer_text="Subnautica Shuffle: Pre-Game",
        )

################################################################################
    @staticmethod
    def cancel_game_start() -> Embed:

        return U.make_embed(
            title="Game Start Cancelled",
            description=(
                "The game start has been cancelled.\n"
                "You may now continue to add players to the lobby.\n"
                f"{U.draw_line(extra=25)}"
            ),
            footer_text="Subnautica Shuffle: Pre-Game",
        )

################################################################################
    @staticmethod
    def game_start() -> Embed:

        return U.make_embed(
            title="Game Starting",
            description=(
                "The game is now loading.\n"
                f"{U.draw_line(extra=25)}\n"
                "Enjoy diving into the depths of Subnautica Shuffle,\n"
                "where resource management and strategic decision-making\n"
                "are key to survival and victory!.\n"
                f"{U.draw_line(extra=25)}"
            ),
            footer_text="Subnautica Shuffle: Loading",
        )

################################################################################
    @staticmethod
    def card_hand(player: SubnauticaPlayer, turn: SubnauticaTurn) -> Embed:

        fields = [
            EmbedField(
                name="Current Turn",
                value=f"Turn {turn.turn} - {player.user.mention}",
                inline=False
            )
        ]

        return U.make_embed(
            title="Your Hand",
            description=(
                "This is your hand of cards.\n"
                f"{U.draw_line(extra=25)}\n"
                "You may take two (2) actions per turn.\n"
                "For more information about your turn options,\n"
                "use the 'Turn Help' button below.\n"
                "You may also use the 'Card Help' button below\n"
                "for more information about the cards in your hand.\n"
                f"{U.draw_line(extra=25)}"
                "TODO: Add more information about the cards here."
                # TODO: Add more information about the cards here.
                f"{U.draw_line(extra=25)}"
            ),
            fields=fields,
            footer_text=f"Subnautica Shuffle: {player.user.name}'s Turn",
        )

################################################################################
    @staticmethod
    def turn_help() -> Embed:

        return U.make_embed(
            title="Turn Help",
            description=(
                "This is a list of the actions you can take on your turn.\n"
                f"{U.draw_line(extra=25)}\n"
            ),
            footer_text="Subnautica Shuffle: Turn Help",
        )

################################################################################
    @staticmethod
    def card_help() -> Embed:

        return U.make_embed(
            title="Card Help",
            description=(
                "This is a list of all the cards and their effects.\n"
                f"{U.draw_line(extra=25)}\n"
            ),
            footer_text="Subnautica Shuffle: Card Help",
        )

################################################################################
    @staticmethod
    def game_log(log: GameLog) -> Embed:

        log_items: List[SubnauticaLogItem] = log.items
        if len(log_items) > 15:
            log_items = log_items[-15:]

        log_body = "\n".join([item.format() for item in log_items])

        return U.make_embed(
            title="Game Log",
            description=(
                f"{U.draw_line(extra=25)}\n"
                f"{log_body}\n"
                f"{U.draw_line(extra=25)}"
            ),
        )

################################################################################
