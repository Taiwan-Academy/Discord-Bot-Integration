class Bot:
    # Virtual function when bot is ready
    async def on_ready(self):
        pass
    
    # Virtual function when bot receive message from user
    async def on_message(self, message):
        pass

    # Virtual function when bot receive message from itself
    async def on_bot_message(self, message):
        pass

    # Virtual function when member update status
    async def on_member_update(self, before, after):
        pass

    # member join abstract function
    async def on_member_join(self, member):
        pass
