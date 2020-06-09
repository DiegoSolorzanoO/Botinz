import discord
import os
from dbHandler import DBManager

from dotenv import load_dotenv
load_dotenv()

dbManager = DBManager()

dbManager.CreateTable()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        channel = self.get_channel(521407366214713368)
        await channel.send('Hello there, general kenobi')

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()

client.run(os.getenv('DISCORD_TOKEN'))