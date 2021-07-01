from API import API
from keep_alive import keep_alive

from IntroductionBot import IntroductionBot

if __name__ == '__main__':
    bots = [IntroductionBot()]
    api = API(bots)

    # run
    keep_alive()
    api.run()