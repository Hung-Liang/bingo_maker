import os
from pathlib import Path

import discord
from discord.ext import commands
from dotenv import load_dotenv

from lib.file_path import BINGO_PATH
from lib.logger import log
from lib.photo_lib import create_bingo_sheet, generate_images

load_dotenv()

discord_token = os.environ.get("discord_token")

intent = discord.Intents.default()
intent.message_content = True

client = commands.Bot(command_prefix='$', intents=intent)


@client.event
async def on_ready():

    log(f'{client.user.name} has connected to Discord!\n', console=True)
    log(f'{client.user} is connected to the following guild:\n', console=True)

    for guild in client.guilds:
        log(f'{guild.name}(id: {guild.id})', console=True)

    generate_images()
    log("Generate images", console=True)


@client.command()
async def doro(ctx):

    user_id = str(ctx.author.id)

    filename = f"{user_id}.png"

    directory = os.listdir(BINGO_PATH)

    file_path = Path(BINGO_PATH, filename)

    if filename not in directory:
        log(f"Create bingo sheet for {user_id}")
        create_bingo_sheet(file_path)

    log(f"Send bingo sheet for {user_id}")
    await ctx.reply(file=discord.File(file_path))


client.run(discord_token)
