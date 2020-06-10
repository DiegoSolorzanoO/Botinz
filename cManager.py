import discord
from dbHandler import DBManager

class CManager:
    def __init__(self, dbManager):
        self.dbManager = dbManager

    async def add(self, message, args):
        if len(args) == 4:
            if self.dbManager.NewAutoMessage(args[2],args[3]):
                await message.channel.send('New trigger added')
            else:
                await message.channel.send('Trigger already used')
        else:
            await message.channel.send('Wrong command usage. //add//<trigger>//<response>')