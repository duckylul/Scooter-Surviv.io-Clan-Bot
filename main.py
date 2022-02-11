
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
import lxml




bot = ComponentsBot(command_prefix='!')
bot.remove_command("help")

bot.load_extension("ping_07")

bot.load_extension("youtube_suggestions")


bot.load_extension("rules")





bot.load_extension("active_clans")




@bot.event
async def on_ready():
    print(f"{bot.user} is ready! Go scooter!!")
    print(discord.__version__)


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
@commands.has_permissions(manage_channels=True, manage_roles=True)
async def scrim_custom_enable(ctx: commands.Context, user: discord.Member):
    """
    A command that enables scrim_custom command.
    """
    
    role = discord.utils.find(lambda r: r.name == 'Scrim Hoster', ctx.message.guild.roles)
    if role not in user.roles:
        embed = discord.Embed(title="You either do not have the role 'Scrim Hoster' in your server, or you do not have the role to enable this command. Once you have the role you can use the command!", colour=0x87CEEB)

        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="The command '!scrim_custom' is avaliable to you!", colour=0x87CEEB)
        
        await ctx.send(embed=embed)

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

@bot.command()
async def helpme(ctx: commands.Context):
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
     
    yeet = ["Dumb", 'gay', 'noob', 'smart', 'chicken','witch', 'bot', 'human', 'duck', 'coward', "dog"]
     
    

    username = user.name
    
    things = random.choice(yeet)
    val = random.randint(1,100)
    embed = discord.Embed(title=f"Rating {user}", description="Rate", colour=0x87CEEB)

    embed.add_field(name="Scooter's rating:", value=f"{username} is %{val} {things}", inline=False)

    
    await ctx.send(embed=embed)  

@bot.command()
async def war_custom(ctx: commands.Context):
      
        
 
      try:   

        await ctx.send("What is the first role name you want to ping? Make sure to include spaces and caps if there is!")
    
        role_1 = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=59.0)
        

        #Asks for which channel to send message too
        await ctx.send("What channel do you want to send too, please put your channel id that you are sending too!")
    
        channel_scrim = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
        


        #Asks for time of the scrim
        await ctx.send("What is the teams that are fighting? ")

        time_scrim = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
         
        #Asks for what mode will be playing in the Scrim
        await ctx.send("What time? ")

        mode_scrim = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)

        #Asks for what type, like 1v1s
        await ctx.send("What type of war(1v1, 2v2, etc)?")

        type_scrim = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)

        #Asks where to find the code
        await ctx.send("Pubs or prestige??")

        code_scrim = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
        
        #Asks for extra information
        await ctx.send("Additional Information? ")

        additional_scrim = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)

      except asyncio.TimeoutError:
        await ctx.send("Oops! You took to long to answer! Try again!")

    
      else:
        #Getting channel to send to!
        #await channel.send(f"{scrim_role.mention}")
        channel = bot.get_channel(int(channel_scrim.content))

        #Making the custom embed

        first_role = get(ctx.guild.roles, name=role_1)


        sky_role = get(ctx.guild.roles, id=925816423702462505)
        pawg_role = get(ctx.guild.roles, id=925821214809817098)
        finnse_role = get(ctx.guild.roles, id=925854049792831510)
        latam_role = get(ctx.guild.roles, id=925864326567460895)
        matrix_role = get(ctx.guild.roles, id=925889234278170635)
        yardent_role = get(ctx.guild.roles, id=925886912185634877)
        gorkers_role = get(ctx.guild.roles, id=925852296024313866)
        bro_role = get(ctx.guild.roles, id=925832175994175498) 
        


        embed = discord.Embed(title="War Info", description="War", colour=0x87CEEB)
      
        embed.add_field(name="Teams fighting:", value="**"+time_scrim.content+"**", inline=False)

        embed.add_field(name="Time:", value="**"+mode_scrim.content+"**", inline=False)

        embed.add_field(name="Type of war( 2v2,3v3, 4v4):", value="**"+type_scrim.content+"**", inline=False)

        embed.add_field(name="Pubs or Prestige", value="**"+code_scrim.content+"**", inline=False)

        embed.add_field(name="Additional Information:", value="**"+additional_scrim.content+"**", inline=False)
         
        #await channel.send(f"{sky_role.mention}{pawg_role.mention}{finnse_role.mention}{latam_role.mention}{matrix_role.mention}{yardent_role.mention}{gorkers_role.mention}{bro_role.mention}")  
        #await channel.send(f"{first_id.mention}{second_id.mention}")

        await channel.send(f"{first_role.mention}")   

        await channel.send(embed=embed)










 
#try to make new scouting material


seconds = 95

#classic solos loop
@tasks.loop(seconds=1)
async def solos_loop():
    global seconds
    if seconds == 0:
      seconds = 95
    else:
      seconds = seconds - 1
      
solos_loop.start()

#starting event loop
@tasks.loop(seconds=1)
async def event_loop():
    global seconds
    if seconds == 0:
      seconds = 95
    else:
      seconds = seconds - 1

@bot.command()
async def scout(ctx: commands.Context):


    await ctx.send("Solos, Squads, Duos? ")

    mode = await bot.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=30.0)
     

    if mode == 'solos' or 'Solos':
       
       embed = discord.Embed(title="Scouting", description="Scouting for new lobbys!", colour=0x87CEEB)

       embed.add_field(name="Mode: ", value="Classic Solos", inline=False)

       embed.add_field(name="Region: ", value = "NA", inline=False)

       embed.add_field(name="Prestige Island", value="True", inline=False)

       embed.add_field(name="Trainee Island", value="False", inline=False)

       embed.add_field(name="Event", value="False", inline=False)

       timestamp = datetime.datetime.utcnow()

       embed.set_footer(text = timestamp, icon_url = "https://i.imgur.com/uZIlRnK.png")

       
     
       print(seconds)

       secs = 95-seconds

       await asyncio.sleep(secs)
       
       await ctx.send("CONNECTED TO NA:")
       await ctx.send("JOIN: " + ctx.author.mention)
       await ctx.send("JOIN: " + ctx.author.mention)
       await ctx.send("JOIN: " + ctx.author.mention)
       await ctx.send("JOIN: " + ctx.author.mention)
       
      

    if mode == 'Squads' or 'squads' or 'Duos' or 'duos':
       await ctx.send("This is not availiable right this momment.") 





keep_alive()        
my_secret = os.environ['TOKEN']
bot.run(my_secret)