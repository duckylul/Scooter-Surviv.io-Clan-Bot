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


bot.load_extension("ping_07")

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

@bot.command()
@commands.has_role("Scrim Hoster")
async def scrim_custom(ctx: commands.Context):
      
        
 
      try:   
        #Asks for which channel to send message too
        await ctx.send("What channel do you want to send too, please put your channel id that you are sending too!")

        channel_scrim = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
    
        #Asks for time of the scrim
        await ctx.send("What is the time of the scrim? ")

        time_scrim = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
         
        #Asks for what mode will be playing in the Scrim
        await ctx.send("What mode is it? ")

        mode_scrim = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)

        #Asks for what type, like 1v1s
        await ctx.send("What type of scrim(1v1, 2v2, etc)?")

        type_scrim = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)

        #Asks where to find the code
        await ctx.send("Where is the code or where to find it??")

        code_scrim = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
        
        #Asks for extra information
        await ctx.send("Additional Information? ")

        additional_scrim = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)

      except asyncio.TimeoutError:
        await ctx.send("Oops! You took to long to answer! Try again!")

    
      else:
        #Getting channel to send to!

        channel = bot.get_channel(int(channel_scrim.content))

        #Making the custom embed


        scrim_role = get(ctx.guild.roles, name='Scrim Ping')
        

        embed = discord.Embed(title="Scrim Info", description=scrim_role.mention, colour=0x87CEEB)
      
        embed.add_field(name="Time:", value="**"+time_scrim.content+"**", inline=False)

        embed.add_field(name="Mode:", value="**"+mode_scrim.content+"**", inline=False)

        embed.add_field(name="Type:", value="**"+type_scrim.content+"**", inline=False)

        embed.add_field(name="Code:", value="**"+code_scrim.content+"**", inline=False)

        embed.add_field(name="Additional Information:", value="**"+additional_scrim.content+"**", inline=False)
         
        await channel.send(f"{scrim_role.mention}")  
        await channel.send(embed=embed)



my_secret = os.environ['TOKEN']
bot.run(my_secret)