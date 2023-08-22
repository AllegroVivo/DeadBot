from __future__ import annotations

import os

from discord import Intents
from dotenv import load_dotenv

from Classes import DeadBot
################################################################################

bot = DeadBot(
    description="For all your Venue needs!",
    intents=Intents.default(),
    debug_guilds=[303742308874977280, 955933227372122173, 1133900477541650696]
)

################################################################################

for filename in os.listdir("Cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"Cogs.{filename[:-3]}")

################################################################################

load_dotenv()

bot.run(os.getenv("DISCORD_TOKEN"))

################################################################################
