# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

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
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'bruh, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == 'hi':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    hru = [
        'Running optimally',
        'running fine',
        (
            'Great, '
            'Awesome!'
        ),
    ]

    if message.content == 'how are you bot?':
        response = random.choice(hru)
        await message.channel.send(response) 

client.run(TOKEN)
