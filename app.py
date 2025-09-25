from flask import Flask, request
import telepot

# === Настройки ===
BOT_TOKEN = "8406911439:AAEmyVmVWq7y4gSYgszuEsSuTOm_ljLf_0Q"   # твой токен
SECRET = "2143secret"   # любое случайное слово/число (защита вебхука)

# === Инициализация бота ===
bot = telepot.Bot(BOT_TOKEN)

# Устанавливаем вебхук (делается 1 раз при старте приложения)
bot.setWebhook("https://Leonid2143t43htrt.pythonanywhere.com/{}".format(SECRET), max_connections=1)

# === Flask ===
app = Flask(__name__)

@app.route('/')
def home():
    return "🤖 Бот работает через WEBHOOK! Отправь /start в Telegram."

@app.route('/{}'.format(SECRET), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if not update:
        return "no update", 400

    if "message" in update:
        chat_id = update["message"]["chat"]["id"]

        if "text" in update["message"]:
            text = update["message"]["text"]
            # Ответ пользователю
            if text == "/start":
                bot.sendMessage(chat_id, "✅ Привет! Бот работает через WEBHOOK на PythonAnywhere.")
            elif text == "/help":
                bot.sendMessage(chat_id, "📋 Доступные команды:\n/start - начало\n/help - помощь")
            else:
                bot.sendMessage(chat_id, f"🔍 Ты сказал: '{text}'")
        else:
            bot.sendMessage(chat_id, "❌ Я понимаю только текстовые сообщения.")

    return "OK", 200
