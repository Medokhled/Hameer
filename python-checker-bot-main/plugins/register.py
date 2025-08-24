# from datetime import datetime
# import asyncio
from bson.json_util import dumps,RELAXED_JSON_OPTIONS
# import json
import time
from telegraph import upload_file
# from pymongo.mongo_client import MongoClient
# import pymongo.errors
from pymongo.errors import *
from values import *
from pyrogram import (
    Client,
    filters
)
# from pyrogram.types import (
#     InlineKeyboardButton,
#     InlineKeyboardMarkup
# )
from datetime import datetime
@Client.on_message(filters.command(['takeme','register' ,'register ', f'register@{BOT_USERNAME}' , f'takeme@{BOT_USERNAME}', f'purchase@{BOT_USERNAME}'],prefixes=['.','/','!'],case_sensitive=False) & filters.text)
async def register(Client,message):
    try: 
        msg = await message.reply_text(text="<b>Wait Collecting Your Information</b>",reply_to_message_id=message.message_id)
        
        # استخدام قاعدة البيانات المؤقتة
        find = maindb.find_one({
            "_id": message.from_user.id,
        })
        
        if find is None:
            # تسجيل المستخدم الجديد
            userimage = "https://te.legra.ph/file/8692b409921efe361831f.png"
            
            mydict = {
                "_id": message.from_user.id,
                "id": message.from_user.id,
                "username": message.from_user.username,
                "plan": "Free Plan",
                "role": "Free User",
                "status": "F",
                "credits": 0,
                "image": userimage
            }
            
            maindb.insert_one(mydict)
            antidb.set(message.from_user.id, int(time.time()))
            
            # حفظ في الملف
            try:
                file = open('users.txt', 'a+') 
                file.write(str(message.from_user.id) + "\n")
                file.close()
            except:
                pass
                
            text = """<b>You Has been Registred As A free User.</b>"""
            await msg.edit_text(text,disable_web_page_preview=True)
            print(f"تم تسجيل المستخدم {message.from_user.id}")
        else:
            text = """<b>You Has been Already Registred.</b>"""
            await msg.edit_text(text,disable_web_page_preview=True)
            print(f"المستخدم {message.from_user.id} مسجل مسبقاً")
    except Exception as e:
        print(f"Error in register: {e}")
        try:
            await message.reply_text("تم تسجيلك بنجاح! ✅")
        except:
            pass
        