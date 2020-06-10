import discord
import os
from dbHandler import DBManager
from cManager import CManager
from dotenv import load_dotenv

load_dotenv()

# Managers initiated
dbManager = DBManager()
cManager = CManager(dbManager)

# Initial tables created
dbManager.CreateTable()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    triggered = dbManager.GetAutoMessageResponse(message.content)
    if triggered:
        await message.channel.send(triggered)
        return

    args = message.content.split("//")
    if len(args) > 1:
        command = args[1]
        if len(args) > 2:
            if command == 'add':
                await cManager.add(message, args)
                return
            if command == 'rm':
                await cManager.rm(message, args)
        else:
            if command == 'ping':
                await message.channel.send('PONG!')

client.run(os.getenv('DISCORD_TOKEN'))