# cog for help commands

import discord
from discord.ext import commands

class Help(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print('We have logged in as {0.user}'.format(self.client))

    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     if message.author == self.client.user:
    #         return

    #     if message.content.startswith('hello'):
    #         await message.channel.send('Hello!')
        
    #     await self.client.process_commands(message)


def setup(client):
    client.add_cog(Help(client))
    print('initialized help.py')