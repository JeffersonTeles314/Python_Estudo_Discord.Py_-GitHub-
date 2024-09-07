import discord
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta

class TestsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='talk')
    async def talk(self,ctx):
        await ctx.channel.send('Olá! Você usou o comando talk!')
        
    @commands.command(name='send_image')
    async def send_image(self,ctx):
        with open('Obama.jpg', 'rb') as f:
            picture = discord.File(f)
            await ctx.channel.send('Aqui está a imagem:', file=picture)

    @commands.Cog.listener()
    async def on_message(self,message):
        # Ignora mensagens do próprio bot
        if message.author == self.bot.user:
            return

        # Verifica se o autor da mensagem está sendo rastreado
        print(message.author.id)
        if message.author.id == 460494790086098945:
            await message.channel.send(f'Estou respondendo a {message.author.mention}: {message.content}')
        
        # Necessário para processar comandos
        await self.bot.process_commands(message)

# @bot.event 
# async def on_message(message):
#     # Ignora mensagens do próprio bot
#     if message.author == bot.user:
#         return

#     # Verifica se o autor da mensagem está sendo rastreado
#     if message.author.id in active_users:
#         await message.channel.send(f'Estou respondendo a {message.author.mention}: {message.content}')
    
#     # Necessário para processar comandos
#     await bot.process_commands(message)