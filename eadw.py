
import discord, asyncio
import random
import string
import os 

from discord.ext import commands


bot = commands.Bot (command_prefix='prefix')

@bot.command()
async def q():
    await message.channel.send('q')

bot.run(os.environ['token'])
