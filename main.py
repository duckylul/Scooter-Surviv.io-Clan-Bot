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



bot = commands.Bot(command_prefix="!")

bot.load_extension("scrim_custom")

@bot.event
async def on_ready():
    print(f"{bot.user} is ready! Go scooter!!")


#Orginal: async def scrim_info(ctx: commands.Context, *, time: str, *args)

@bot.command()
@commands.is_owner()
async def setstatus(ctx: commands.Context):
    """Set the bot's status."""

    await ctx.send("Type the bot's status: ")

    status = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
    
    await ctx.send("What type of status(Game, Watching, Listening)")

    status_type = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
    
    if status_type.content.lower() == "game":
        await bot.change_presence(activity=discord.Game(name=status.content))

    if status_type.content.lower() == "watching":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status.content))

    if status_type.content.lower() == "listening":
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status.content))
   
    
@bot.command()
async def scrim_custom_enable(ctx: commands.Context, user: discord.Member):
    """
    A command that enables scrim_custom command.
    """
    
    role = discord.utils.find(lambda r: r.name == 'Scrim Hoster', ctx.message.guild.roles)
    if role not in user.roles:
        await ctx.send("You either do not have the role 'Scrim Hoster' in your server, or you do not have the role to enable this command. Once you have done that the command will be avaliable to you!")
    else:
        await ctx.send("The command is avaliable to you!")



my_secret = os.environ['TOKEN']
bot.run(my_secret)