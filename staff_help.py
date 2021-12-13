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
        staff_embed = discord.Embed(title="Staff Help For Scooter", color=0xf47fff)
        
        staff_embed.add_field(name="!scrim_custom_embed",
		             value="Generate 1 unchecked nitro/nitro classic code")



def setup(bot: commands.Bot):
    bot.add_cog(satff_help_embed(bot))