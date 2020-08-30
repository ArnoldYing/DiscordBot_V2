import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# load the .env file for bot token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# create the client object
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Bot Online')
    print(f'Username: {client.user.name}')
    print(f'Client ID: {client.user.id}')

# commands to load, unload, and reload cog extensions
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

# initialize all the cogs extensions before running the bot
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)