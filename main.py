from flask import Flask
from threading import Thread

from API import API
from Bot1 import Bot1
from IntroductionBot import IntroductionBot

if __name__ == '__main__':
    bots = [Bot1(), IntroductionBot()]
    api = API(bots)
    api2 = API()

    api.print("API1")
    api2.print("API2")

    API().run()

# ## Flask app to keep alive
# app = Flask('')

# @app.route('/')
# def home():
#     return "Hello. I am alive!"

# def run():
#   app.run(host='0.0.0.0',port=8080)

# if __name__ =='__main__':
#     thread = Thread(target=run)
#     thread.start()