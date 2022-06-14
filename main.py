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
from datetime import datetime
from keep_alive import keep_alive
import requests
from pretty_help import DefaultMenu, PrettyHelp





bot = ComponentsBot(command_prefix='!', help_command=PrettyHelp())


@bot.event
async def on_ready():
    print(f"{bot.user} is ready! Go scooter!!")
    print(discord.__version__)


bot.remove_command("help")

bot.load_extension("ping_07")




bot.load_extension("jokes")

bot.load_extension("rules")






menu = DefaultMenu(page_left="⬅️", page_right="➡️", active_time=60)


ending_note = "The ending note from {ctx.bot.user.name}\nFor command {help.clean_prefix}{help.invoked_with}"

bot.help_command = PrettyHelp(menu=menu, ending_note=ending_note)


#Orginal: async def scrim_info(ctx: commands.Context, *, time: str, *args)







@bot.command()
@commands.is_owner()
async def setstatus(ctx: commands.Context):
    """Set the bot's status. Only Ilikeducks#2405 can do this!!"""

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
async def war_results(ctx: commands.Context):   
        """Creates a war result embed with your specfic requirments."""

        
        

        team1_players = {}
    
        try: 
            
           await ctx.send("What is the first team?")
        
           team1 = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
 
           await ctx.send("What's the second team?")

           team2 = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)

           await ctx.send("What's the score. First team - Second team(Example: 4-0, 4-1)")
            
           score = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)

           team1 = team1.content  

           #loop 
           x = 0
           while x == 0:
              
              
             
                
              await ctx.send(f"Who played for {team1}. Note: Once you finished with all the players, say 'done' ")
              players = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)

              players = players.content  

              if players == 'done':
                  x = 1
 
              await ctx.send(f"How many rounds did {players} play?")


              round = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0) 

              if players == 'done':
                  x = 1

              else:
                  round = round.content
                  team1_players[players]=round
                  
               
       
        
        except asyncio.TimeoutError:
           await ctx.send("You took too long to answer, try again!")  
        

        else:
            
            team2 = team2.content
            score = score.content
            
            embed = discord.Embed(title=f"War Results: {team1} {score} {team2} ",color=0xf47fff)
        
             


            


            await ctx.send(embed=embed)
























@bot.command()
async def helpme(ctx: commands.Context):
    """Scooter gives advice. Just tell it what's wrong! Do !helpme"""

    
    advice = ["Get help", "Adopt a duck", "Move to another country", "Rob a bank!", "Eat a spider", "Go see a witch", "Do yoga on a volcano", "Watch a chessy romantic show", "Get a girlfriend", "Play surviv.io", "Watch Mrbeast", "Look up Hom Tolland", "Lock yourself in a cabinent", "Give $1 to a random stranger!"]

    try:
      embed = discord.Embed(title="What seems to be the problem? ", color=0xf47fff)
      
      await ctx.send(embed=embed)

      problem = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
    
    except asyncio.TimeoutError:
        await ctx.send("You took too long to answer, looks like you don't want my advice :((")
    
    else:
        problem = problem.content
        
       
        advice_rando=random.choice(advice)
        embed = discord.Embed(title = f"**Response to: `{problem}`  **", color=0xf47fff)
        embed.add_field(name="**Scooter's Advice**",
		             value=f"{advice_rando}")
        
        await ctx.send(embed=embed)

@bot.command()
async def rate(ctx: commands.Context, user: discord.Member):
    """Scooter rates a user!! Do !rate @user"""
    yeet = ["Dumb", 'gay', 'noob', 'smart', 'chicken','witch', 'bot', 'human', 'duck', 'coward', "dog"]
     
    

    username = user.name
    
    things = random.choice(yeet)
    val = random.randint(1,100)
    embed = discord.Embed(title=f"Rating {user}", description="Rate", colour=0x87CEEB)

    embed.add_field(name="Scooter's rating:", value=f"{username} is %{val} {things}", inline=False)

    
    await ctx.send(embed=embed)  


@bot.command()
async def about_scooter(ctx: commands.Context, user: discord.Member):
    pass
   
   










keep_alive()        
my_secret = os.environ['TOKEN']
bot.run(my_secret)