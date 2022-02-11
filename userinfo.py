from datetime import datetime
from typing import Optional

import discord 
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord import Embed, Member
from discord.ext import commands, tasks
import discord
import string
import sys
import asyncio
import random
import os
import requests
import time
from discord.utils import get
from discord_components import DiscordComponents, Button, ButtonStyle, ComponentsBot

from keep_alive import keep_alive
import requests
import lxml


bot = commands.Bot(command_prefix="!")


class Info(commands.Cog):
    """get user's info"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @command(name="userinfo", aliases=["memberinfo","ui", "mi"])
    async def user_info(self, ctx, target: Optional[Member]):
        target = target or ctx.author

        embed = Embed(title="User information", colour=target.colour, timestamp=datetime.utcnow())

        embed.set_thumbnail(url=target.avatar_url)

        await ctx.send(embed=embed)


    @command(name="serverinfo", aliases=["guildinfo", "si", "gi"])
    async def server_info(self, ctx):
        pass


    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("info")
        
    



def setup(bot: commands.Bot):
    bot.add_cog(Info(bot))