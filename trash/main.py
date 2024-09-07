import discord
import dotenv
from discord.ext import commands
import os

dotenv.load_dotenv()

cliente = commands.Bot(command_prefix='.')

@cliente.event
async def on_ready():
    print('O Bot Está Pronto')
    
cliente.run(os.getenv("API_KEY"))
