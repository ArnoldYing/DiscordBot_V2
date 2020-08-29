import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# load the .env file for bot token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# create the client object
client = commands.Bot(command_prefix='!')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.online, activity=discord.Game("with a fidget spinner"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    
    await client.process_commands(message)

client.run(TOKEN)