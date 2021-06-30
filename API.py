import discord
from os import environ

_intents = discord.Intents.default()
_intents.members = True
_token = environ['DISCORD_TOKEN']
_client = discord.Client(intents=_intents)

class _API_Base(type):
    __instance = None
    _bots = None
    def __call__(cls, *args, **kwargs):
        print("API call")
        if cls.__instance is None:
            print("API Init")
            cls.__instance = super(_API_Base, cls).__call__(*args, **kwargs)
        return cls.__instance

class API(metaclass=_API_Base):
    def __init__(self, bots=None) -> None:
        if not (bots is None):
            print("API bots")
            _API_Base._bots = bots

## Other methods defines below
    def print(self, msg): # FIXME: Test
        print("API print {}".format(msg))
    
    def run(self):
        print("API run")
        _client.run(_token)

## Client events
@_client.event
async def on_ready():
    print("Client ready")
    if not (_API_Base._bots is None):
        for bot in _API_Base._bots:
            bot.on_ready()

@_client.event
async def on_message(message):
    print("Client message")
    if not (_API_Base._bots is None):
        for bot in _API_Base._bots:
            bot.on_message(message)

