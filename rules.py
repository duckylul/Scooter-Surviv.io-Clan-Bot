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


class rules_embed(commands.Cog):
    """Embed for staff help"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    
    @bot.command()
    @commands.is_owner()
    async def rules(self, ctx: commands.Context):   
        embed = discord.Embed(title="Rules", color=0xf47fff)
        
        embed.add_field(name="**1. Be respectful**",
		             value="You must respect all users, regardless of your liking towards them. Treat others the way you want to be treated.")
        embed.add_field(name="**2. No Inappropriate Language**",
		             value="The use of profanity should be kept to a minimum. However, any derogatory language towards any user is prohibited.")
        embed.add_field(name="**3. No spamming**",
		             value="Don't send a lot of small messages right after each other. Do not disrupt chat by spamming.")
        embed.add_field(name="**4. No pornographic/adult/other NSFW material**", value="This is a community server and not meant to share this kind of material.")
        embed.add_field(name="**5. No advertisements**",
		             value="You must respect all users, regardless of your liking towards them. Treat others the way you want to be treated.")
        embed.add_field(name="**6. No offensive names and profile pictures**",
		             value="You must respect all users, regardless of your liking towards them. Treat others the way you want to be treated.")
        embed.add_field(name="**7. Server Raiding**",
		             value="You must respect all users, regardless of your liking towards them. Treat others the way you want to be treated.")
        embed.add_field(name="**8. Direct & Indirect Threats**",
		             value="You must respect all users, regardless of your liking towards them. Treat others the way you want to be treated.")
        embed.add_field(name="**9. Follow the Discord Community Guidelines**",
		             value="You must respect all users, regardless of your liking towards them. Treat others the way you want to be treated.")
        embed.add_field(name="**10. Do not join voice chat channels without permission of the people already in there**",
		             value="You must respect all users, regardless of your liking towards them. Treat others the way you want to be treated.")
        embed.add_field(name="**The Admins and Mods will Mute/Kick/Ban per discretion. If you feel mistreated dm an Admin and we will resolve the issue.**", value="Please be honest!")
		            
        embed.add_field(name="**All Channels will have pinned messages explaining what they are there for and how everything works. If you don't understand something, feel free to ask!**",  value="You can also open a ticket")
        embed.add_field(name="**Your presence in this server implies accepting these rules, including all further changes. These changes might be done at any time without notice, it is your responsibility to check for them**",  value="Thank you so much for joining this server!")

        await ctx.send(embed=embed)
        



def setup(bot: commands.Bot):
    bot.add_cog(rules_embed(bot))