import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = '-')

client.run(os.environ['token'])
