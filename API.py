import discord
from os import environ, truncate
import asyncio
from Singleton import Singleton

__intents = discord.Intents.default()
__intents.members = True

_token = environ['DISCORD_TOKEN']
_client = discord.Client(intents=__intents)

class API(metaclass=Singleton):
    _bots = None
    def __init__(self, bots=None) -> None:
        if not (bots is None):
            self._bots = bots

    ## Other methods defines below
    def run(self):
        print("Run API")
        _client.run(_token)

    async def client_await(self):
        await _client.wait_for('message')

    async def add_role(self,author: discord.member.Member ,role_id: int , guild: int = 0):
        if type(author) == discord.member.Member:
            verifiedRole = discord.utils.get(author.guild.roles, id = role_id)
            member = author
        else:
            # KEY, if from private channel(DM), then message.author will be discord.user.User,  which don't belong to any server
            # So in that case guild will be required. Need to find the server and member
            guild = _client.get_guild(guild)
            member = guild.get_member(author.id)
            verifiedRole = discord.utils.get(guild.roles, id = role_id)
            
        if member:            
            await member.add_roles(verifiedRole)
        else:
            print("NOTE: cannot find such member, please check whether guild(server id) is provided")

    async def wait_for_reaction(self, msg_user_id):
        def check(reaction, user):
            return str(user.id) == str(msg_user_id)

        try:
            reaction, user = await _client.wait_for('reaction_add', timeout=60.0, check=check)
            return reaction
        except asyncio.TimeoutError:
            return "Time out"
        else:
            return "Null"



        # return reaction, user


## Client events
@_client.event
async def on_ready():
    api = API()
    if not (api._bots is None):
        print('We have logged in as {0.user}'.format(_client))
        for bot in api._bots:
            await bot.on_ready()

@_client.event
async def on_message(message):
    api = API()
    if not (api._bots is None):
        for bot in api._bots:
            if message.author.id == _client.user.id:
                await bot.on_bot_message(message)
            else:
                await bot.on_message(message)

@_client.event
async def on_member_join(member):
    api = API()
    if not (api._bots is None):
        for bot in api._bots:
            await bot.on_member_join(member)

