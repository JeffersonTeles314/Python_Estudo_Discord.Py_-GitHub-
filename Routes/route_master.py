import discord
from discord.ext import commands
from Routes.tests import TestsCog
# Substitua 'your_token_here' pelo token do seu bot

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    await load_cogs()

async def load_cogs():
    await bot.add_cog(TestsCog(bot))  # Add the FunCog instance

