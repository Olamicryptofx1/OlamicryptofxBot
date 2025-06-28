import telebot
from telebot import types
from datetime import datetime, timedelta
import os

API_TOKEN = 'YOUR_BOT_TOKEN_HERE' ADMIN_ID = 6955958431

bot = telebot.TeleBot(API_TOKEN)

Keep track of users and expiration dates

subscribed_users = {}

@bot.message_handler(commands=['start']) def send_welcome(message): markup = types.ReplyKeyboardMarkup(resize_keyboard=True) markup.row("📩 Get Access to Signal", "📞 Contact Admin") bot.send_message(message.chat.id, "Welcome to Olamicryptofx Signal Bot.\n\nYou'll receive 2–4 setups weekly on Gold (XAUUSD), Bitcoin (BTCUSD), and NASDAQ (US100).\n\nChoose an option below to continue:", reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == "📞 Contact Admin") def contact_admin(message): bot.send_message(message.chat.id, "You can reach the admin directly at @Olamicryptofx01.")

@bot.message_handler(func=lambda msg: msg.text == "📩 Get Access to Signal") def get_access(message): bot.send_message(message.chat.id, "Please make payment of ₦30,000 or $20 (USDT BEP20).\n\nBank: Kuda Microfinance\nAccount Number: 2003917268\nName: Aderinto Abdulmuiz Olamiposi\n\nUSDT (BEP20): 0x655844b3e11101716135cdb037ea02973dc8ba1f\n\nAfter payment, send your payment screenshot and name here.")

@bot.message_handler(content_types=['photo', 'text']) def handle_payment_proof(message): if message.chat.id != ADMIN_ID: bot.forward_message(ADMIN_ID, message.chat.id, message.message_id) bot.send_message(message.chat.id, "Payment proof sent! Please wait for admin confirmation.") elif message.chat.id == ADMIN_ID and message.text.startswith("confirm"): try: parts = message.text.split() user_id = int(parts[1]) months = int(parts[2]) expire_date = datetime.now() + timedelta(days=30 * months) subscribed_users[user_id] = expire_date bot.send_message(user_id, f"✅ Subscription confirmed! You’ll receive signals for {months} month(s).") bot.send_message(ADMIN_ID, f"User {user_id} confirmed for {months} month(s).") except: bot.send_message(ADMIN_ID, "❌ Invalid confirmation format. Use: confirm USER_ID MONTHS") else: bot.send_message(message.chat.id, "❗ Please use the menu buttons.")

@bot.message_handler(commands=['broadcast']) def broadcast(message): if message.chat.id != ADMIN_ID: return msg = bot.send_message(ADMIN_ID, "Send the broadcast message (text only):") bot.register_next_step_handler(msg, send_broadcast)

def send_broadcast(message): for user_id, expire_date in subscribed_users.items(): if datetime.now() < expire_date: try: bot.send_message(user_id, message.text) except: pass bot.send_message(ADMIN_ID, "✅ Broadcast sent.")

@bot.message_handler(func=lambda msg: True) def catch_all(message): bot.send_message(message.chat.id, "❗ Invalid input. Please use the buttons provided.")

bot.polling()

