from __future__ import annotations

from datetime   import datetime
from discord    import Colour, Embed, Member, User
from typing     import TYPE_CHECKING, Optional, Union

from Assets     import BotImages

if TYPE_CHECKING:
    from Classes import Position, SubnauticaPlayer, SubnauticaGame
################################################################################

__all__ = (
    "ErrorMessage",
    "InvalidSalaryError",
    "EmployeeNotFoundError",
    "TooManyPositionsError",
    "PositionNotFoundError",
    "EmployeeAlreadyExistsError",
    "EmployeeNotFoundAtClockInError",
    "NotClockedInError",
    "AlreadyClockedInError",
    "PositionNotFoundError",
    "AlreadyInGameError",
)

################################################################################
class ErrorMessage(Embed):
    """A subclassed Discord embed object acting as an error message."""

    def __init__(
        self,
        *,
        title: str,
        message: str,
        solution: str,
        description: Optional[str] = None
    ):

        super().__init__(
            title=title,
            description=description if description is not None else Embed.Empty,
            colour=Colour.red()
        )

        self.add_field(
            name="What Happened?",
            value=message,
            inline=True,
        )

        self.add_field(
            name="How to Fix?",
            value=solution,
            inline=True
        )

        self.timestamp = datetime.now()
        self.set_thumbnail(url=BotImages.ErrorFrog)

################################################################################
class InvalidSalaryError(ErrorMessage):

    def __init__(self, value: str):
        super().__init__(
            title="Invalid Salary Value",
            description=f"**{value}** is not a valid salary value.",
            message="The value you provided couldn't be converted into a valid number.",
            solution=(
                "Please provide a valid salary value. This must be digits and "
                "may only end in '`k`' or '`m`' to represent thousands or millions"
                "respectively."
            )
        )

################################################################################
class EmployeeNotFoundError(ErrorMessage):

    def __init__(self, user: Union[Member, User]):
        super().__init__(
            title="Employee Not Found",
            description=f"**{user.mention}** is not an employee.",
            message="The user you provided is not an employee.",
            solution=(
                "Please provide a valid employee or contact management to add one."
            )
        )

################################################################################
class TooManyPositionsError(ErrorMessage):

    def __init__(self):
        super().__init__(
            title="Too Many Positions",
            message="You have too many job Positions registered.",
            solution=(
                "You may only register up to 20 Positions. Please remove one "
                "before adding another by using `/position status`."
            )
        )

################################################################################
class PositionExistsError(ErrorMessage):

    def __init__(self, position: Position):
        super().__init__(
            title="Position Already Exists",
            message=f"A position with the name `{position.name}` already exists.",
            solution="Please provide a different name for your position."
        )

################################################################################
class EmployeeAlreadyExistsError(ErrorMessage):

    def __init__(self, user: Union[Member, User]):
        super().__init__(
            title="Employee Already Exists",
            message=f"{user.mention} is already an employee.",
            solution="Please provide a different user."
        )

################################################################################
class EmployeeNotFoundAtClockInError(ErrorMessage):

    def __init__(self, user: Union[Member, User]):
        super().__init__(
            title="Clock In/Out Error",
            message=(
                f"{user.mention} is not an employee at this venue."
            ),
            solution="Please contact your manager for assistance. ♥"
        )

################################################################################
class NotClockedInError(ErrorMessage):

    def __init__(self, user: Union[Member, User]):
        super().__init__(
            title="Clock Out Error",
            message=(
                f"{user.mention} is not clocked in."
            ),
            solution="Please clock in before clocking out silly~."
        )

################################################################################
class AlreadyClockedInError(ErrorMessage):

    def __init__(self, user: Union[Member, User]):
        super().__init__(
            title="Clock In Error",
            message=(
                f"{user.mention} is already clocked in."
            ),
            solution="Please clock out before clocking in silly~."
        )

################################################################################
class PositionNotFoundError(ErrorMessage):

    def __init__(self, name: str):
        super().__init__(
            title="Position Not Found",
            message=f"A position with the name `{name}` could not be located.",
            solution="Please confirm you've spelled the position name correctly."
        )

################################################################################
class AlreadyInGameError(ErrorMessage):

    def __init__(self, player: SubnauticaPlayer, game: SubnauticaGame):
        super().__init__(
            title="Already in Game",
            description=f"Game ID: {game.id}",
            message=(
                f"{player.user.mention} is already in a game of Subnautica Shuffle."
            ),
            solution="Please finish your current game before starting a new one."
        )

################################################################################
