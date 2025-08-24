import logging
from pyrogram import Client, filters

# إعداد التسجيل
logging.basicConfig(level=logging.INFO)

# إنشاء البوت
bot = Client(
    'test_bot',
    api_id=29784596,
    api_hash="4f330d47c4fa2a9732caa0036942c5a9",
    bot_token="8059528086:AAFIZLlNJzo_nUplHlXzjyShla-DsT0RNYw"
)

@bot.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("مرحباً! البوت يعمل 🎉")

@bot.on_message(filters.command("test"))
async def test_command(client, message):
    await message.reply_text("اختبار البوت يعمل! ✅")

print("تشغيل البوت...")
bot.run()