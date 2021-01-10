# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
        
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    hru = [
        'Running optimally',
        'Running fine',
        (
            'Great, '
            'Awesome!'
        ),
    ]
    hi = [
        'Hi',
        'What\'s up?',
        (
            'Great, '
            'Awesome!'
        ),
    ]
    creator = [
        'You made me',
        'You are the creator',
        (
            'Okay,'
            'Right...'
        ),
    ]
     gamesevents = [
        'Orcacon',
        'CES',
        'Otakufest',
    ]

    if message.content == 'games events ':
        response = random.choice(gamesevents)
        await message.channel.send(response) 
    if message.content == 'how are you bot?':
        response = random.choice(hru)
        await message.channel.send(response)
    if message.content == 'hi bot':
        response = random.choice(hi)
        await message.channel.send(response)
    if message.content == 'who made you bot?':
        response = random.choice(creator)
        await message.channel.send(response)

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

client.run(TOKEN)
bot.run(TOKEN)
