import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='py?')

@bot.event
async def on_ready():
    print('Iniciado como:\n{0.user.name}\n{0.user.id}'.format(bot))

@bot.command
async def hola(ctx):
  await ctx.send('Hola.')

bot.run(nope)
