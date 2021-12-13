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



class scrim_custom_embed(commands.Cog):
    """In progress?"""

    def __init__(self, bot: commands.Bot):
      self.bot = bot

    @bot.command()
    @commands.has_role("Scrim Hoster")
    async def scrim_custom(self, ctx: commands.Context):
      
        
 
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


      @scrim_custom.error
      async def example_error(self, ctx: commands.Context, error: commands.CommandError):
        """Handle errors for the example command."""

        if isinstance(error, commands.CommandOnCooldown):
            message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
        elif isinstance(error, commands.MissingPermissions):
            message = "You are missing the required permissions to run this command!"
        elif isinstance(error, commands.MissingRequiredArgument):
            message = f"Missing a required argument: {error.param}"
        elif isinstance(error, commands.ConversionError):
            message = str(error)
        elif isinstance(error, commands.error.MissingRole):                
            message = f"You need to make a assign the role called 'Scrim Hoster'"
        else:
            return

        await ctx.send(message)  







def setup(bot: commands.Bot):
    bot.add_cog(scrim_custom_embed(bot))