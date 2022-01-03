from discord.ext import commands
import discord
import string
import sys
import asyncio
import random
import os
import requests
import time
from discord.utils import get

bot = commands.Bot(command_prefix="!")


class staff_help_embed(commands.Cog):
    """Embed for staff help"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @bot.command()
    async def staff_help(self, ctx: commands.Context):   
        embed = discord.Embed(title="Help For Scooter", color=0xf47fff)
        
        embed.add_field(name="!scrim_custom",
		             value="Makes a custom embed as your choice. It will ask you for what channel id to send at, mode, time, what time of scrim, and additional info! To enable this command do !scrim_custom_enable ")

        embed.add_field(name="!scrim_custom_enable",
		             value="Enables the scrim_custom. Must have in your server role Scrim Hoster and Scrim Ping for this to work. And the role must be assigned to you the Scrim Hoster to allow you to make the custom embed")
                

        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(staff_help_embed(bot))