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
            print("API bots") # FIXME:
            self._bots = bots

## Other methods defines below
    def print(self, msg): # FIXME: Test
        print("API print {}".format(msg))
    
    def run(self):
        print("API run") # FIXME:
        _client.run(_token)

## Client events
@_client.event
async def on_ready():
    print("Client ready") # FIXME:
    api = API()
    if not (api._bots is None):
        for bot in api._bots:
            bot.on_ready()

@_client.event
async def on_message(message):
    print("Client message") # FIXME:
    api = API()
    if not (api._bots is None):
        for bot in api._bots:
            bot.on_message(message)
