import discord
import random
import asyncio
from discord.ext import commands, tasks
from discord.ext.commands import Bot

__version__ = '0.0.1'

pr = ['src!']
bot = commands.Bot(command_prefix=pr)
bot.remove_command('help')

@bot.event
async def on_ready():
    change_staus.start()
    print('The bot is running!')
    if bot.user.id == userid: #put your user ID here or else the code isnt going to work u dont need '' or "" for this
        bot.dev = True
    else:
        bot.dev = False

    print('Logged in as..')
    print(f'Bot-Name: {bot.user.name}')
    print(f'Bot-ID: {bot.user.id}')
    print(f'Dev Mode: {bot.dev}')
    print(f'Discord Version: {discord.__version__}') 
    print(f'Bot Version: {__version__}')
    bot.AppInfo = await bot.application_info()
    print(f'Owner: {bot.AppInfo.owner}')
    print('------')

@tasks.loop(seconds=5)
async def change_staus():
    status = [
        'github', 'src!', 'https://github.com/PythonJoshua',
        'Open Source by 7o_#9066', 'HmMmMm'
    ]
    await bot.change_presence(activity=discord.Game(random.choice(status)))

@bot.command()
async def src(ctx):
    embed = discord.Embed(
        title="Open Source by 7o_#9066",
        description="bot",
        colour=ctx.author.colour  # remove my credits means stupid
    )  # code by 7o_#9066
    embed.set_footer(text="Open SRC")
    await ctx.send(embed=embed)

bot.run("token here")
