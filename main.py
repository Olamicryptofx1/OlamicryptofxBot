import telebot
from telebot import types
from datetime import datetime, timedelta
import os

# Use environment variables for token and admin ID (set them on Render)
API_TOKEN = os.getenv("TELEGRAM_API_KEY")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = telebot.TeleBot(API_TOKEN)

# Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("📩 Get Access to Signal", "📞 Contact Admin")
    bot.send_message(
        message.chat.id,
        "👋 Welcome to OlamicryptoFX Signal Bot!\n\nUse the buttons below to continue.",
        reply_markup=markup
    )

# Handle unknown text input
@bot.message_handler(func=lambda message: True)
def handle_unknown(message):
    bot.send_message(
        message.chat.id,
        "❗ Please use the buttons below. Free-typed messages are not supported yet."
    )

# Start polling
print("✅ Bot is polling...")
bot.polling()
