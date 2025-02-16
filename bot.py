import discord
from discord.ext import commands
from discord import app_commands
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
    # Sync the app commands with the Discord server
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands to the server.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

class MyBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='buy', description='Information on how to buy')
    async def buy(self, interaction: discord.Interaction):
        await interaction.response.send_message('Thank you for your interest in buying! Please visit our website to make a purchase.')

    @app_commands.command(name='getscript', description='Get the script link')
    async def getscript(self, interaction: discord.Interaction):
        await interaction.response.send_message('Here is the script you requested: [link to script]')

    @app_commands.command(name='giverole', description='Give a role to a member (Admin only)')
    @app_commands.default_permissions(administrator=True)
    async def giverole(self, interaction: discord.Interaction, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await interaction.response.send_message(f'Role {role.name} has been given to {member.mention}')

    @app_commands.command(name='buyerrole', description='Assign the "Buyer" role to yourself')
    async def buyerrole(self, interaction: discord.Interaction):
        role = discord.utils.get(interaction.guild.roles, name='Buyer')
        if role:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f'Role {role.name} has been assigned to you.')
        else:
            await interaction.response.send_message('Role "Buyer" does not exist.')

    @app_commands.command(name='howtobuy', description='Guide on how to buy')
    async def howtobuy(self, interaction: discord.Interaction):
        await interaction.response.send_message('To buy, follow these steps:\n1. Visit our website.\n2. Select the product you want to purchase.\n3. Follow the checkout process.\n4. Contact our support if you need assistance.')

bot.tree.add_command(MyBot(bot).buy)
bot.tree.add_command(MyBot(bot).getscript)
bot.tree.add_command(MyBot(bot).giverole)
bot.tree.add_command(MyBot(bot).buyerrole)
bot.tree.add_command(MyBot(bot).howtobuy)

bot.run(DISCORD_TOKEN)
