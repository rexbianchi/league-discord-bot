import discord
import os

from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("TOKEN")


bot = commands.Bot(command_prefix="!")



@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.event
async def on_message(message):
    
    if message.content == ('!ping'):
        await message.channel.send('Pong')
        
    if message.content == ('!hello'):
        await message.channel.send('Hello')

    await bot.process_commands(message)

@bot.command(
    # ADDS THIS VALUE TO THE $HELP PRINT MESSAGE.
	help="Looks like you need some help.",
	# ADDS THIS VALUE TO THE $HELP MESSAGE.
	brief="Prints the list of values back to the channel."
)
async def print(ctx,*args):
        response = ""

        for arg in args:
                response = response + " " + arg

        await ctx.channel.send(response)

bot.run(TOKEN)
