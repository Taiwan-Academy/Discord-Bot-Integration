import discord
from os import environ

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
        _client.run(_token)

## Client events
@_client.event
async def on_ready():
    api = API()
    if not (api._bots is None):
        for bot in api._bots:
            bot.on_ready()

@_client.event
async def on_message(message):
    api = API()
    if not (api._bots is None):
        for bot in api._bots:
            bot.on_message(message)
