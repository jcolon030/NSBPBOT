from discord.ext import commands
import discord
from webScrapper import *

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello\nHello")

@bot.command()
async def physicsNews(ctx):
    refresh()
    for i in range(len(links)):
        await ctx.send(f"\n\nTopic:\n\n{titles[i]}\n\n{links[i]}\n")



bot.run(f"REPLACE_WITH_KEY")
