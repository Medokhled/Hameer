#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id=29784596, #get it from https://my.telegram.org/auth
    api_hash="4f330d47c4fa2a9732caa0036942c5a9", #get it from https://my.telegram.org/auth
    bot_token="8059528086:AAFIZLlNJzo_nUplHlXzjyShla-DsT0RNYw", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
    