import discord
import DB
from keep_alive import keep_alive
from discord.ext import commands

import asyncio

# intents are used Bot configuration to limit its
intents = discord.Intents.default()
intents.members = True

# Initialize discord bot instance
client = discord.Client(intents=intents)
token = os.environ['DISCORD_TOKEN']

# Connect to sqlite db
# Default connect to 'data.sqlite', can pass in db_name to connect to different DB
# db ==> connection to db, cur ==> use cursor to execute query
db, cur = DB.connect_DB()


# Triggered when client is ready
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# Triggered when user send_message on public/private channel
@client.event
async def on_message(message):
    # author will be different class if the user send message in public/ private channel
    author = message.author
    msg = message.content

    start_msg = 'Hi user'
    if msg.startswith('$hello'):
        # send start_msg to the channel that 'message' is sent
        await message.channel.send(start_msg)

        # DM the author the start_msg
        await author.send(start_msg)

# Triggered when a new member join this server
@client.event
async def on_member_join(member):

    role_ID = 848537536716734474 # Role_Id for certain role

    # once the user join, add him as certain role
    await add_role(member, role_ID)

# Self-defined function
# -------------------
async def add_role(member: discord.Member, role_ID, role_name=None):
    # Use role_id or role_name to find the registered role
    role = discord.utils.get(member.guild.roles, id = role_ID)
    # role = discord.utils.get(member.guild.roles, name = role_name)

    await member.add_roles(verifiedRole)

    # KEY should use asyncio.sleep, other will sleep the whole program
    await asyncio.sleep(5)

    role_name = role.name if role_name == None else role_name
    await member.send("You've been already added {} role".format(role_name))


@commands.has_role(role_name)
async def remove_role(member: discord.Member,role_ID, role_name=None):
    role = discord.utils.get(member.guild.roles, name = role_name)
    await member.remove_roles(role)

    # KEY should use asyncio.sleep, other will sleep the whole program
    await asyncio.sleep(5)

    role_name = role.name if role_name == None else role_name
    await member.send("You've been already deprived {} role".format(role_name))


if __name__ =='__main__':
    # Trigger client by token
    client.run(token)
    keep_alive()
