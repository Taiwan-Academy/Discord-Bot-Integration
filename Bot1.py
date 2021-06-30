from Bot import Bot

class Bot1(Bot):
    def on_message(self, message):
        print("Bot1 message: [{}] {}".format(message.author, message.content))