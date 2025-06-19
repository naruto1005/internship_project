import os
import django
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')  
django.setup()
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegrambot.models import TelegramUser
from asgiref.sync import sync_to_async  
@sync_to_async
def save_user(username, chat_id):
    TelegramUser.objects.get_or_create(username=username, chat_id=chat_id)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_user = update.effective_user
    username = tg_user.username or tg_user.first_name or f"user_{tg_user.id}"
    chat_id = tg_user.id

    await save_user(username, chat_id)
    await update.message.reply_text(f"Hello {username}! You're registered ✅")

def main():
    app = ApplicationBuilder().token("7460397654:AAFP5UEFjciF9nAMZ28ve5OUgNaa-t6bbR4").build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 Bot is running... Press Ctrl+C to stop")
    app.run_polling()
if __name__ == '__main__':
    main()
