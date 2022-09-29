from http import client
import discord  
from discord.ext import commands
import os
from dotenv import load_dotenv 


bot = discord.Client(intents=discord.Intents.default())
client = commands.Bot(command_prefix="!", intents=discord.Intents.default())
token = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
     print("Logged in as a bot {0.user}".format(bot))

@client.command()
async def hi(ctx):
    await ctx.send("hello")
    

bot.run(f"MTAxOTczMzcxODE5NTI0NTE4Ng.Gx1jof.UjBEiwV3HpQg2ld_-PMjXRkRE_FNP1Yo3o9afM")