from __future__ import annotations

from discord import Embed, EmbedField
from typing import TYPE_CHECKING, List

from Classes.Game import GameLog
from Classes.Game.LogItem import SubnauticaLogItem
from Utils import Utilities as U
from Utils import *

if TYPE_CHECKING:
    from Classes import Application, PriorWorkExp
################################################################################

__all__ = ("ApplicationMessageManager",)

################################################################################
class ApplicationMessageManager:

    def __init__(self):

        pass

################################################################################
    @staticmethod
    def application_status(app: Application) -> Embed:

        if len(app.about) > 250:
            aboutme = f"{app.about[:250]}..."
        else:
            aboutme = app.about

        if not app.work_experience:
            workexp = (
                "`No Previous Work Experience Had Been Set`\n"
                "`Click Below to Set Work Experience`"
            )
        else:
            workexp = ApplicationMessageManager.work_exp_summary(app.work_experience)

        if not app.rp_choice:
            rpexp = (
                "`No Roleplay Experience Had Been Set`\n"
                "`Click Below to Set Roleplay Experience`"
            )
        else:
            rpexp = ApplicationMessageManager.rp_exp_summary(app.roleplay_experience)

        fields = [
            EmbedField(
                name="__Applying For__",
                value=", ".join([f"`{p.name}`" for p in app.positions]),
                inline=False,
            ),
            EmbedField(
                name="__Character Name__",
                value=(f"`{app.name}`" if app.name else str(NS)),
                inline=True
            ),
            EmbedField(
                name="__Age__",
                value=(f"`{app.age}`" if app.age else str(NS)),
                inline=True
            ),
            EmbedField(
                name="__Pronouns__",
                value=(
                    ", ".join([f"`{p.name}`" for p in app.pronouns])
                    if app.pronouns else str(NS)
                ),
                inline=True
            ),
            EmbedField(
                name="__Data Center/Home World__",
                value=(
                    f"`{app.datacenter.name}`/`{app.world.name}"
                    if app.datacenter is not NS else str(NS)
                ),
                inline=True
            ),
            EmbedField(
                name="__Timezone__",
                value=(f"`{app.timezone.proper_name}`" if app.timezone is not NS else str(NS)),
                inline=True
            ),
            EmbedField(
                name="__Languages__",
                value=(
                    ", ".join([f"`{l.name}`" for l in app.languages])
                    if app.languages else str(NS)
                ),
                inline=True
            ),
            EmbedField(
                name="__About Me__",
                value=aboutme,
                inline=False
            ),
            EmbedField(
                name="__Work Experience__",
                value=workexp,
                inline=False
            ),
            EmbedField(
                name="__Roleplay Experience__",
                value=rpexp,
                inline=False
            ),
        ]

        return U.make_embed(
            title=f"Application Status for __{app.user.display_name}__",
            description=f"{U.draw_line(extra=25)}",
            thumbnail_url=app.image if app.image else Embed.Empty,
            fields=fields,
        )

################################################################################
    @staticmethod
    def work_exp_summary(work_experience: List[PriorWorkExp]) -> str:

        ret = ""

        for exp in work_experience:
            ret += (
                f"`{exp.position:<20}` | `{exp.venue:<20}` | `{exp.time:<15}`\n"
            )

        if ret:
            ret = (
                f"__`{'Position':<20}`__ | __`{'Venue:':<20}`__ | __ `{'__Length of Time__':<15}`\n"
            ) + ret

        return ret

################################################################################
    @staticmethod
    def set_timezone(tz: TimeZone) -> Embed:

        return U.make_embed(
            title="Set Your Timezone",
            description=(
                "__**Required:**__\n"
                "Please select your timezone from the dropdown below.\n"
                "If your timezone is not listed, please select `Other`.\n"
                f"{U.draw_line(extra=25)}"
                "__**Currently Selected:**__\n"
                f"`{tz.proper_name}`\n\n"

                f"{U.draw_line(extra=25)}"
            ),
        )

################################################################################
    @staticmethod
    def set_pronouns(pronouns: List[Pronoun]) -> Embed:

        pronoun_value = [f"`{p.name}`" for p in pronouns]

        return U.make_embed(
            title="Set Your Pronouns",
            description=(
                "__**Required:**__\n"
                "Please select your pronouns from the dropdown below.\n"
                "If your pronouns are not listed, please select `Other`.\n"
                f"{U.draw_line(extra=25)}"
                "__**Currently Selected:**__\n"
                f"`{'/'.join(pronoun_value)}`\n\n"

                f"{U.draw_line(extra=25)}"
            ),
        )

################################################################################
    @staticmethod
    def set_languages(languages: List[Language]) -> Embed:

        language_value = [f"`{l.name}`" for l in languages]

        return U.make_embed(
            title="Set Your Languages",
            description=(
                "__**Required:**__\n"
                "Please select your languages from the dropdown below.\n"
                "If your languages are not listed, please select `Other`.\n"
                f"{U.draw_line(extra=25)}"
                "__**Currently Selected:**__\n"
                f"`{'/'.join(language_value)}`\n\n"

                f"{U.draw_line(extra=25)}"
            ),
        )

################################################################################
    @staticmethod
    def set_dcworld(datacenter: DataCenter, world: WorldEnum) -> Embed:

        return U.make_embed(
            title="Set Your Data Center and Home World",
            description=(
                "__**Required:**__\n"
                "Please select your data center and home world from the "
                "dropdowns below.\n"
                "After selecting your data center, another dropdown will "
                "appear with the worlds available on that data center.\n"
                f"{U.draw_line(extra=25)}"
                "__**Currently Selected:**__\n"
                f"`{datacenter.name}`/`{world.name}`\n\n"

                f"{U.draw_line(extra=25)}"
            ),
        )

################################################################################
    @staticmethod
    def set_work_exp(work_exp: List[PriorWorkExp]) -> Embed:

        pass

################################################################################
