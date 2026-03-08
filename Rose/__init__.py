import aiohttp
import pymongo
from pyrogram import Client

from config import Config

app = Client(
    "bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)

bot = Client(
    "user",
    api_id=Config.API_ID1,
    api_hash=Config.API_HASH1,
)

BOT_ID = int(Config.BOT_TOKEN.split(':')[0])
OWNER_ID = Config.OWNER_ID
BOT_NAME = "Rose"
BOT_USERNAME = Config.BOT_USERNAME
aiohttpsession = None
MOD_LOAD = None
MOD_NOLOAD = None
DB_URI = Config.MONGO_URL
MONGO_URL = Config.MONGO_URL
LOG_GROUP_ID = Config.LOG_GROUP_ID
myapp = pymongo.MongoClient(MONGO_URL)
db = myapp["Rose"]
dbn = myapp

async def eor(message, **kwargs):
    return await message.reply_text(**kwargs)

class DummyARQ:
    async def search(self, query):
        return {"result": "dummy"}

arq = DummyARQ()