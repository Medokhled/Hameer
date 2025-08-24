# 🚀 إعداد البوت - Card Checker Bot

## ✅ ما تم إنجازه:
- ✅ API ID: `29784596`
- ✅ API Hash: `4f330d47c4fa2a9732caa0036942c5a9`
- ✅ Bot Token: `8059528086:AAFIZLlNJzo_nUplHlXzjyShla-DsT0RNYw`

## 🔄 ما يحتاج إلى تحديث:

### 1. قاعدة بيانات MongoDB
اذهب إلى [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register) وأنشئ قاعدة بيانات مجانية:

1. سجل حساب جديد
2. أنشئ مشروع جديد
3. أنشئ قاعدة بيانات مجانية
4. أضف IP Address: `0.0.0.0/0` (للوصول من أي مكان)
5. أنشئ مستخدم وكلمة مرور
6. انسخ Connection String

### 2. قاعدة بيانات Redis
اذهب إلى [Redis Cloud](https://redis.com/try-free/) وأنشئ قاعدة بيانات مجانية:

1. سجل حساب جديد
2. أنشئ قاعدة بيانات مجانية
3. انسخ Host, Port, Password

### 3. تحديث BOT_USERNAME
احصل على اسم المستخدم للبوت من @BotFather

## 📝 تحديث الملفات:

### في ملف `values.py`:
```python
# استبدل هذه القيم بالقيم الحقيقية
mongourl = 'mongodb+srv://username:password@cluster.mongodb.net/bot?retryWrites=true&w=majority'
antidb = redis.Redis(host='redis-host.com', port=12345, password='redis-password')
BOT_USERNAME = 'your_bot_username'
```

## 🏃‍♂️ تشغيل البوت:

```bash
# تثبيت المكتبات المطلوبة
pip install -r requirements.txt

# تشغيل البوت
python main.py
```

## ⚠️ تحذير:
هذا البوت مخصص لفحص البطاقات الائتمانية. استخدمه فقط لأغراض تعليمية أو اختبارية مع البيانات الوهمية.

## 📞 الدعم:
إذا واجهت أي مشاكل، راجع ملف README.md الأصلي للحصول على تعليمات مفصلة.