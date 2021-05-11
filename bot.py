import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '*', intents = intents)

@client.event
# When it's ready
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

client.run('ODQxMDc2ODAzMDQ4MzA4NzQ3.YJhf0A.t_6K8DodVK46_Zn4WQ6XeG9Mqi8')