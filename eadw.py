import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')
@client.event
async def on_ready():

client.run(os.environ['token'])
