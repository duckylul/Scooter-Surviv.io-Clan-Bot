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


class help_embed(commands.Cog):
    """Embed for staff help"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @bot.command()
    async def h(self, ctx: commands.Context):   
        embed = discord.Embed(title="Help For Scooter", color=0xf47fff)
        
        embed.add_field(name="!staff_help",
		             value="Command only for staff! Help for the staff commands.")

        embed.add_field(name="!funhelp",
		             value="Help for some fun things scooter can do! Avaliable to everyone!")
                

        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(help_embed(bot))