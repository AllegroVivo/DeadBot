from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING, Any, Optional

from discord import ButtonStyle
from discord.ui import Button

if TYPE_CHECKING:
    pass
################################################################################

__all__ = ("SetStyleButton",)

################################################################################
class SetStyleButton(Button):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

################################################################################
    def set_style(self, attribute: Optional[Any]) -> None:

        if attribute:
            if isinstance(attribute, Enum):
                match attribute.value:
                    case 0:
                        self.style = ButtonStyle.secondary
                    case _:
                        self.style = ButtonStyle.primary
            else:
                self.style = ButtonStyle.primary
        else:
            self.style = ButtonStyle.secondary

################################################################################
