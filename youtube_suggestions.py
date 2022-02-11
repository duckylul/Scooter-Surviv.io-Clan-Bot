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

bot = commands.Bot(command_prefix='!')

class components_py(commands.Cog):
    """Buttons"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

   

    @commands.command()
    async def youtubesug(self, ctx):

      youtube_survivio = [
        "https://www.youtube.com/c/sv98gaming",#SV-98 Gaming
        "https://www.youtube.com/c/GAMERIO1/", #GAMERIO
        "https://www.youtube.com/c/TTargetYT", #Target
        "https://www.youtube.com/c/silverdotware" #Sliverdotware
      ]
      
      youtuber_survivio = random.choice(youtube_survivio)
     
      if youtuber_survivio == "https://www.youtube.com/c/GAMERIO1/":
          link = 'https://www.youtube.com/c/GAMERIO1/'
          watch = 'https://www.youtube.com/watch?v=rFhmVJcZoHA'

      if youtuber_survivio == "https://www.youtube.com/c/TTargetYT":
          link = 'https://www.youtube.com/c/TTargetYT'
          watch = 'https://www.youtube.com/watch?v=bg9JKaKYj18'

      if youtuber_survivio == "https://www.youtube.com/c/sv98gaming":
          link = 'https://www.youtube.com/c/sv98gaming'
          watch = 'https://www.youtube.com/watch?v=OhGxFgmIq-k'
    
      if youtuber_survivio == "https://www.youtube.com/c/silverdotware":
          link = 'https://www.youtube.com/c/sliverdotware'
          watch = 'https://www.youtube.com/watch?v=1FhXKhYcvLc'

      components = [
        [
            Button(label='Report', style=ButtonStyle.red, custom_id='Report'),
            Button(label='Watch', style=ButtonStyle.URL, url = watch),
            Button(label='Subscribe', style=ButtonStyle.URL, url = link)
            
        ]
      ]

      await ctx.send(youtuber_survivio
      , components=components)

    @commands.Cog.listener()
    async def on_button_click(self, interaction):
      
      timestamp = datetime.now()
      if interaction.custom_id == "Report":
         print('Button Command Reported')
         if interaction.custom_id=="Report":

            with open('youtube_reports.txt', 'w') as f:
               f.write("A user has reported a youtuber please look into it! Time reported: " + str(timestamp) )
               f.close()
            await interaction.send(f'`You have reported this youtuber! Unnesscary reports would result in a punishment!`')


def setup(bot: commands.Bot):
    bot.add_cog(components_py(bot))

# Try now