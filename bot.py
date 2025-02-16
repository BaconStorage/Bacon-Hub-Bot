import discord
from discord.ext import commands
import os
import webserver

DISCORD_TOKEN = os.environ['discordkey']

intents = discord.Intents.default()
intents.message_content = True

webserver.keep_alive()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='Buy')
async def buy(ctx):
    await ctx.send('Thank you for your interest in buying! Please visit our website to make a purchase.')

@bot.command(name='Getscript')
async def getscript(ctx):
    await ctx.send('Here is the script you requested: [link to script]')

@bot.command(name='GiveRole')
@commands.has_permissions(administrator=True)
async def giverole(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f'Role {role.name} has been given to {member.mention}')

@bot.command(name='BuyerRole')
async def buyerrole(ctx):
    role = discord.utils.get(ctx.guild.roles, name='Buyer')
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f'Role {role.name} has been assigned to you.')
    else:
        await ctx.send('Role "Buyer" does not exist.')

@bot.command(name='Howtobuy')
async def howtobuy(ctx):
    await ctx.send('To buy, follow these steps:\n1. Visit our website.\n2. Select the product you want to purchase.\n3. Follow the checkout process.\n4. Contact our support if you need assistance.')

# Register the commands with the command list
@bot.event
async def setup_hook():
    await bot.add_cog(BotCommands(bot))

class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Buy')
    async def buy(self, ctx):
        await ctx.send('Thank you for your interest in buying! Please visit our website to make a purchase.')

    @commands.command(name='Getscript')
    async def getscript(self, ctx):
        await ctx.send('Here is the script you requested: [link to script]')

    @commands.command(name='GiveRole')
    @commands.has_permissions(administrator=True)
    async def giverole(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await ctx.send(f'Role {role.name} has been given to {member.mention}')

    @commands.command(name='BuyerRole')
    async def buyerrole(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name='Buyer')
        if role:
            await ctx.author.add_roles(role)
            await ctx.send(f'Role {role.name} has been assigned to you.')
        else:
            await ctx.send('Role "Buyer" does not exist.')

    @commands.command(name='Howtobuy')
    async def howtobuy(self, ctx):
        await ctx.send('To buy, follow these steps:\n1. Visit our website.\n2. Select the product you want to purchase.\n3. Follow the checkout process.\n4. Contact our support if you need assistance.')

bot.run(DISCORD_TOKEN)
