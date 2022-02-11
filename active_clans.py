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
bot = commands.Bot(command_prefix="!")


class activeclans(commands.Cog):
    """Looks for active clans"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @bot.command()
    async def active_clans(self, ctx: commands.Context):   
        timestamp=datetime.utcnow()

        active_clans =[
            '**CSL Competitve Surviv.io League** | `Link`: https://discord.gg/invite/j2kWtXuhhQ ',

            '**N.A.R.S Scrims** | `Link`: https://discord.com/invite/tRtsWpEuua '



        ]

        random_clan = random.choice(active_clans)
     
        
        if random_clan == "**CSL Competitve Surviv.io League** | `Link`: https://discord.gg/j2kWtXuhhQ":
          link = 'https://discord.gg/j2kWtXuhhQ'
          

        if random_clan == "**N.A.R.S Scrims** | `Link`: https://discord.com/tRtsWpEuua ":
          link = 'https://discord.com/tRtsWpEuua'
         

        time_r = random.randint(1,6)


        components = [
          [
            Button(label='Report', style=ButtonStyle.red, custom_id='Report'),
            Button(label='Join', style=ButtonStyle.URL, url = link),
            
          ]
        ] 
        embed = embed = discord.Embed(title="Searching", color=0xf47fff)
        embed.add_field(name="Searching...", value="This could take up to 6 seconds! Please be patient. If you are getting the same link over and over again, that means no other clans can be found!")
        await ctx.send("`-------------------------------------------------`")
        await ctx.send(embed=embed)

        time.sleep(int(time_r))


        
        await ctx.send(random_clan
         , components=components)

        @commands.Cog.listener()
        async def on_button_click(self, interaction):
      
           timestamp = datetime.now()
           if interaction.custom_id == "Report":
              print('User reported server!')
           if interaction.custom_id=="Report":
  
              with open('server_reports.txt', 'w') as f:
                f.write("A user has reported server please look into it! Time reported: " + str(timestamp) )
                f.close()
                await interaction.send(f'`You have reported this server! Unnesscary reports would result in a punishment!`')

           

        




def setup(bot: commands.Bot):
    bot.add_cog(activeclans(bot))
