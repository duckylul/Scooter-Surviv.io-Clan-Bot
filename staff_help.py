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
    async def shelp(self, ctx: commands.Context):   
        
        embed = discord.Embed(title="Help For Scooter", color=0xf47fff)
        
        embed.add_field(name="**!rate**",
		             value="How to use? `ex. !rate @Ilikeducks`  You must ping a user you want to rate, then it rate that person! ex. @Ilikeducks is %99 a duck. This command is mainly use to make people laugh!!!")

        embed.add_field(name="!helpme",
		             value="How to use? `ex. !helpme` This will ask you `What's wrong` then you will type in something. Then it will give it's personal advice :joy: ")

        
        embed.add_field(name="!scout",
		             value=`"Warning: Command is still under construction. There is a few bugs with the **api** and sometimes will give you a new lobby sometimes no. This is still under testing.` How to use? `ex. !scout` This will ask you if you want to scout Classic solos, duos, or squads, or regular events. You choose one and it will send you an embed of what you told it to scout. Then it will ping you when it's time to join the new lobby!! ")
                

        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(staff_help_embed(bot))