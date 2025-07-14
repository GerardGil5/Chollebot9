import os
import telegram
from deal_fetcher import fetch_deals
from subscription_manager import notify_users
from config import BOT_TOKEN, CHANNEL_ID

bot = telegram.Bot(token=BOT_TOKEN)

def main():
    print("🤖 Bot iniciado...")
    deals = fetch_deals()
    for deal in deals:
        message = f"🔥 OFERTA DETECTADA:\n{deal['title']}\n💰 Precio: {deal['price']}\n🔗 {deal['url']}"
        try:
            bot.send_message(chat_id=CHANNEL_ID, text=message)
            notify_users(deal)
        except Exception as e:
            print(f"❌ Error enviando mensaje: {e}")

if __name__ == "__main__":
    main()
from config import BOT_TOKEN, CHANNEL_ID
print(f"🔐 BOT_TOKEN: {BOT_TOKEN}")
print(f"📣 CHANNEL_ID: {CHANNEL_ID}")
