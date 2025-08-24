# ملف إعدادات مؤقت للاختبار
# استبدل هذه القيم بالقيم الحقيقية قبل التشغيل

# إعدادات قاعدة البيانات
MONGO_URI = "mongodb+srv://username:password@cluster.mongodb.net/bot?retryWrites=true&w=majority"
REDIS_HOST = "redis-host.com"
REDIS_PORT = 12345
REDIS_PASSWORD = "redis-password"

# إعدادات البوت
BOT_USERNAME = "your_bot_username"

# تعليمات التحديث:
print("""
🔧 تعليمات تحديث الإعدادات:

1. اذهب إلى https://www.mongodb.com/cloud/atlas/register
   - أنشئ حساب مجاني
   - أنشئ قاعدة بيانات
   - انسخ Connection String

2. اذهب إلى https://redis.com/try-free/
   - أنشئ حساب مجاني
   - أنشئ قاعدة بيانات
   - انسخ Host, Port, Password

3. احصل على BOT_USERNAME من @BotFather

4. استبدل القيم في ملف values.py بالقيم الحقيقية

5. شغل البوت: ./run.sh
""")