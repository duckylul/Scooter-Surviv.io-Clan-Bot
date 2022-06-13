from discord.ext import commands, tasks
import discord
import asyncio
import random
import os
import requests
import time
from datetime import datetime
from discord.utils import get
from discord_components import Button, ButtonStyle
import pyjokes

bot = commands.Bot(command_prefix='!')

class jokes_py(commands.Cog):
    """Buttons"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

   

    @commands.command()
    async def jokes(self, ctx: commands.Context):
      """Tells you funny jokes! Do !jokes""" 
      #sumjokes = [
       # "`Don't do drugs, too expensive.`",
       # "`You want joke? Here is joke. You are a failure`",
       # "`A duck went to the store and bought a scooter.` ",
        #"`My dolphin puns are terrible on porpoise.`",
       # "`When my son told me to stop impersonating a flamingo, I had to put my foot down.`"
     # ]
      
      #jokes = random.choice(sumjokes)
     
      jokes = pyjokes.get_joke(language="en", category="all")

      components = [
        [
            Button(label='Like', style=ButtonStyle.green, custom_id='Like Joke'),
            Button(label='Dislike', style=ButtonStyle.red, custom_id='Dislike'),
            #Button(label='Subscribe', style=ButtonStyle.URL, url = link)
            
        ]
      ]

      await ctx.send(jokes
      , components=components)

    @commands.Cog.listener()
    async def on_button_click(self, interaction):
      
      timestamp = datetime.now()
      if interaction.custom_id == "Like Joke":
         with open('joke_likes_dislike.txt', 'w') as f:
              f.write("User liked a joke  | Time liked: " + str(timestamp) )
              f.close()
         await interaction.send(f'`You have liked the joke`')
        
      if interaction.custom_id=="Dislike":

         with open('joke_likes_dislike.txt', 'w') as f:
              f.write("User Disliked a joke | Time Disliked + str(timestamp)")
              f.close()
         await interaction.send(f'`You have disliked to joke`')   


def setup(bot: commands.Bot):
    bot.add_cog(jokes_py(bot))