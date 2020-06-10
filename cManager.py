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

    async def rm(self, message, args):
        if not message.channel.permissions_for(message.author).administrator:
            await message.channel.send('You do not have permission for that')
        else:
            if len(args) == 3:
                if self.dbManager.DeleteAutoMessage(args[2]):
                    await message.channel.send('Trigger deleted')
                else:
                    await message.channel.send('Trigger does not exist')
            else:
                await message.channel.send('Wrong command usage. //rm//<trigger>')

    async def reset(self, message, args):
        if not message.channel.permissions_for(message.author).administrator:
            await message.channel.send('You do not have permission for that')
        else:
            self.dbManager.ResetDatabase()
            await message.channel.send('Database was reset')