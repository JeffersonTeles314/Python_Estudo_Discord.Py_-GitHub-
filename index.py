import discord
from discord.ext import commands

cliente = commands.Bot(command_prefix='.')

@cliente.event
async def on_ready():
    print('O Bot Está Pronto')
    
cliente.run('NjUwNzczNjg1NDkzMzAxMjU4.GlQRwM.5a4vEUbqhoE1HWc1-_5w-lbXFcY5IxkTaZrTys')
