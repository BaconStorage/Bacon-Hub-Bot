import os

from discord.ext import commands


@commands.Bot(command_prefix = '#!').event
async def on_ready():
    print(f'Successfully logged in as {client.user}')


@client = commands.Bot(command_prefix = '#!')
.event
async def on_message(message):
    await client.process_commands(message)


# Commands

@client = commands.Bot(command_prefix = '#!')
.command()
async def hello(ctx):
    await ctx.channel.send(f'Hello! {ctx.author}')



token = process.env.TOKEN
client.run(token)
