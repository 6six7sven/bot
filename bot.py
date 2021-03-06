# bot.py
import os
import json
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import requests

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()
bot = commands.Bot(command_prefix='!')

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote  = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

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
    msg = message.content

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
        (
            'CES', 
            'IEM',
         ),
    ]
    fauginfo = [
        'On 26 January , this year',
        'Very soon',
    ]
    amongusinfo = [
        'New update will be havying some antihacking perks ',
        'New update will remove many bugs',
    ]
    ps5info = [
        'It is the first playstation with an internal SSD ',
        'It has a large heat dissipater vent',
    ]
    ludooffer = [
        'I could, if I had some Artificial Intelligence also ',
        'Go ahead, you play and enjoy',
    ]
    lamebot = [
        'Oh so you think that I am lame ',
        'You tell me how to become so cool like you',
        'Let me see if you can teach me something to overcome this',
    ]
    happy_words = ["happy", "grateful", "lovely"]
    starter_appreciators = ["great to see you happy!", "thats really nice!"]
    creators = ["!creators"]
    starter_creators = ['Aryaman', 'Guneet', 'Sushant', 'Punit', 'Neeraj', 'Ayush', 'Chris']
    sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]
    starter_encouragements = ["cheer up!", "hang in there!", "you are a great person! - bot."]
    greetgm = ["good morning"]
    starter_gm = ["Good morning", "A very good morning", "A good morning to you"]
    greetgn = ["good night"]
    starter_gn = ["Good night", "sweet dreams!", "A good night to you"]
    greetga = ["good afternoon"]
    starter_ga =  ["Good afternoon", "A very good afternoon", "A good afternoon to you"]
    greetev = ["good evening"]
    starter_ev = ["Good evening", "A very good evening", "A good evening to you"]
    if message.content == 'this bot is so lame':
        response = random.choice(lamebot)
        await message.channel.send(response) 
    if message.content == 'want to play ludo?':
        response = random.choice(ludooffer)
        await message.channel.send(response) 
    if message.content == 'tell me about ps5':
        response = random.choice(ps5info)
        await message.channel.send(response)    
    if message.content == 'among us new update':
        response = random.choice(amongusinfo)
        await message.channel.send(response) 
    if message.content == 'faug trailer release date':
        response = random.choice(fauginfo)
        await message.channel.send(response) 
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
    if message.content.startswith('!inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    
    if any(word in message.content for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))
    if any(word in message.content for word in happy_words):
        await message.channel.send(random.choice(starter_appreciators))
    if any(word in message.content for word in creators):
        await message.channel.send(starter_creators)
    if any(word in message.content for word in greetgm):
        await message.channel.send(random.choice(starter_gm))
        print({client.user.name})
    if any (word in message.content for word in greetga):
        await message.channel.send(random.choice(starter_ga))
    if any (word in message.content for word in greetev):
        await message.channel.send(random.choice(starter_ev))
    if any (word in message.content for word in greetga):
        await message.channel.send(random.choice(starter_gn))
    
        

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
