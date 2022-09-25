from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", "1945966", cast=int)
API_HASH = config("API_HASH", "6b73197f50512e26f5ebd42e73c3315f")
BOT_TOKEN = config("BOT_TOKEN", "5170301552:AAGQvSED9eQhe6YHzEg3PyjHDZtnMZqq4eE")
BOT_UN = config("BOT_UN", "wetdudubot")
AUTH_USERS = config("AUTH_USERS", "5143506371", cast=int)
LOG_CHANNEL = config("LOG_CHANNEL", "linux_rep0")
LOG_ID = config("LOG_ID", "-1001702681627")
FORCESUB = config("FORCESUB", "-1001163244391")
FORCESUB_UN = config("FORCESUB_UN", "akimaxmovies")
ACCESS_CHANNEL = config("ACCESS_CHANNEL", "-1001707154332")
MONGODB_URI = config("MONGODB_URI", "mongodb+srv://ticel98214:asdfggjkl@cluster0.hm6jsk4.mongodb.net/?retryWrites=true&w=majority")

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
