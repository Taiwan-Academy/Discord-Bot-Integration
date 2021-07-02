from API import API
from DB import DB
from keep_alive import keep_alive

from IntroductionBot import IntroductionBot

if __name__ == '__main__':
    bots = [IntroductionBot()]
    api = API(bots)
    db1 = DB()
    # db Usage: db.create(), db.add() ..... 

    # run
    keep_alive()
    api.run()