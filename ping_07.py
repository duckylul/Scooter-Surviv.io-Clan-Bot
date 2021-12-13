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




class ping_07(commands.Cog):
    """Test API Discord Ping"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @bot.command()
    async def ping(ctx: commands.Context):   
       start_time = time.time()
       message = await ctx.send("Testing Ping...")
       end_time = time.time()
     
       await message.edit(content=f"Pong! {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")





def setup(bot: commands.Bot)
    bot.add_cog(ping_07(bot))
