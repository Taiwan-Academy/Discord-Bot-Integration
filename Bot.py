class Bot:
    def __init__(self) -> None:
        print(self)

    async def on_ready(self):
        print("Bot ready") # FIXME:

    async def on_message(self, message):
        print("Bot message") # FIXME:

    # member join abstract function
    async def on_member_join(self, member):
        print('')
