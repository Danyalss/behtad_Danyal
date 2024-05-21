import os
import random
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Your bot's token (use environment variable for security)
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

user_data = {}

async def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    await update.message.reply_text(f'سلام {user.first_name}! به بات خوش آمدید!')

async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('این یک بات آزمایشی است.')

async def sms_bomber(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("شماره مورد نظر را وارد کنید:")
    user_data[update.message.chat_id] = 'awaiting_number'

async def handle_message(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    text = update.message.text

    if chat_id in user_data and user_data[chat_id] == 'awaiting_number':
        phone_number = text
        user_data[chat_id] = phone_number
        for _ in range(100):
            message_body = f'پیام رندوم شماره {random.randint(1, 1000)}'
            await update.message.reply_text(message_body)
        await update.message.reply_text("100 پیام به شماره مورد نظر ارسال شد.")
        user_data.pop(chat_id, None)
    else:
        await update.message.reply_text("دستور نامعتبر است. لطفا دوباره امتحان کنید.")

def main() -> None:
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("sms_bomber", sms_bomber))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()
