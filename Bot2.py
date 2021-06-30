from Bot import Bot

class Bot2(Bot):
    def on_ready(self):
        print("Bot2 ready")

    def on_message(self, message):
        print("Bot2 message: [{}] {}".format(message.author, message.content))