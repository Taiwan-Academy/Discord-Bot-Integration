from Bot import Bot

class IntroductionBot(Bot):
    
    def on_ready(self):
        print("IntroductionBot ready")

    def on_message(self, message):
        print("IntroductionBot message: [{}] {}".format(message.author, message.content)) # FIXME: