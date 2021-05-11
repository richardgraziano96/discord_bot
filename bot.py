import discord, logging, typing
from discord.ext import commands

#Sets the prexfix, tokens and guild intents so the bot can run
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '!!', intents = intents)
with open('token.txt') as f:
    TOKEN = f.readline()

#All debugging and errors
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

#Bot is online
@client.event
#Prints when bot is ready
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#User joined server
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

#User left/kicked/banned from server
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

#Ping command
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

#Clear command (currently set to clear 5 messages)
@client.command()
async def clear(ctx, ammount = 5):
    await ctx.channel.purge(limit = ammount)

#Kick user
async def kick(ctx, members : discord.Member, *, reason = None):
    await members.kick(reason = reason)

#Ban user(s)
@client.command()
async def ban(ctx, members : commands.Greedy[discord.Member],
                   delete_days : typing.Optional[int] = 0, *,
                   reason : str):
    """Mass bans members with an optional delete_days parameter"""
    for member in members:
        await member.ban(delete_message_days=delete_days, reason=reason)
        await ctx.send(f'Banned {member.mention}')

#Unban a user
@client.command()
async def unban(ctx, *, members):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = members.split('#')
    
    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

#Run the bot
client.run(TOKEN)