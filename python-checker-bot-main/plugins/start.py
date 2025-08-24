from datetime import datetime
# import os
# from bson.json_util import dumps
# import time
# import pymongo
# from telegraph import upload_file
# import redis
# import pymongo.errors
from pymongo.errors import *
from values import *
from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

REPLY_MARKUP  = InlineKeyboardMarkup([
    [
    InlineKeyboardButton('📒 MY ACCOUNT 📒', callback_data='myacc'),
    InlineKeyboardButton('🚪 GATES 🚪', callback_data='gates')
    ],
    [
        InlineKeyboardButton('🔒 CLOSE 🔒', callback_data='close')
    ]
])
@Client.on_message(filters.command(['start', f'start@{BOT_USERNAME}'],prefixes=['.','/','!'],case_sensitive=False) & filters.text)
async def start(Client, message):
    try:
        await Client.send_chat_action(message.chat.id, "typing")
        if message.reply_to_message is not None:
            message.text = message.reply_to_message.text
        dt_string = datetime.now().strftime(" %B %Y And Time Is %H-%M %p")
        day = make_ordinal(datetime.now().strftime("%d"))
        caption = f"""
<b>{get_part_of_day()} <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>[<code>{message.from_user.id}</code>],
How Are You?
I Am Jocasta. The Multi Functional Bot For You.
Today Is {day} Of {dt_string}.
Check And Click Down For More</b>    
"""
        await Client.send_message(chat_id=message.chat.id,text=caption,disable_web_page_preview=True,reply_to_message_id=message.message_id,reply_markup=REPLY_MARKUP)
        print(f"تم إرسال رسالة start للمستخدم {message.from_user.id}")
    except Exception as e:
        print(f"Error in start command: {e}")
        try:
            await Client.send_message(chat_id=message.chat.id, text="مرحباً! البوت يعمل الآن 🎉")
        except:
            print("فشل في إرسال رسالة الخطأ")
    # try: 
    #     find = maindb.find_one({
    #         "_id": message.from_user.id,
    #     })
    # except DuplicateKeyError as e:
    #     print("Dublicate")
    # except pymongo.errors.PyMongoError as e:
    #     await Client.send_message(chat_id=loggp,text=e)
    #     print(e)
    #     quit()
    # except Exception as e:
    #     await Client.send_message(chat_id=loggp,text=e)
    #     print(e)
    #     quit()  
    
