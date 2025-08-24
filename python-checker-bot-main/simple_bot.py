import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime

# إعداد التسجيل
logging.basicConfig(level=logging.INFO)

# إنشاء البوت
bot = Client(
    'simple_bot',
    api_id=29784596,
    api_hash="4f330d47c4fa2a9732caa0036942c5a9",
    bot_token="8059528086:AAFIZLlNJzo_nUplHlXzjyShla-DsT0RNYw"
)

# أزرار القائمة
REPLY_MARKUP = InlineKeyboardMarkup([
    [
        InlineKeyboardButton('📒 MY ACCOUNT 📒', callback_data='myacc'),
        InlineKeyboardButton('🚪 GATES 🚪', callback_data='gates')
    ],
    [
        InlineKeyboardButton('🔒 CLOSE 🔒', callback_data='close')
    ]
])

@bot.on_message(filters.command("start"))
async def start_command(client, message):
    try:
        await client.send_chat_action(message.chat.id, "typing")
        
        # الحصول على الوقت
        dt_string = datetime.now().strftime(" %B %Y And Time Is %H-%M %p")
        
        # رسالة الترحيب
        caption = f"""
<b>مرحباً <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>[<code>{message.from_user.id}</code>]!
كيف حالك؟
أنا Jocasta. البوت متعدد الوظائف لك.
اليوم هو {datetime.now().strftime("%d")} من {dt_string}.
تحقق واضغط أدناه للمزيد</b>    
"""
        await client.send_message(
            chat_id=message.chat.id,
            text=caption,
            disable_web_page_preview=True,
            reply_to_message_id=message.message_id,
            reply_markup=REPLY_MARKUP
        )
    except Exception as e:
        print(f"Error in start command: {e}")
        await message.reply_text("مرحباً! البوت يعمل الآن 🎉")

@bot.on_message(filters.command("register"))
async def register_command(client, message):
    await message.reply_text("تم تسجيلك بنجاح! ✅")

@bot.on_message(filters.command("test"))
async def test_command(client, message):
    await message.reply_text("اختبار البوت يعمل! ✅")

@bot.on_callback_query()
async def callback_handler(client, callback_query):
    if callback_query.data == "myacc":
        await callback_query.answer("حسابك")
        await callback_query.message.reply_text("معلومات حسابك 📊")
    elif callback_query.data == "gates":
        await callback_query.answer("البوابات")
        await callback_query.message.reply_text("قائمة البوابات 🚪")
    elif callback_query.data == "close":
        await callback_query.answer("تم الإغلاق")
        await callback_query.message.delete()

print("تشغيل البوت البسيط...")
bot.run()