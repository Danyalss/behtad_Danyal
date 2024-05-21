from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Your bot's token
TELEGRAM_BOT_TOKEN = '7058724141:AAGxes7Qhb8JMcyNXlT_2vhjtQN3nf3V-OI'

user_data = {}

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f'سلام {user.first_name}! به بات خوش آمدید!')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('این یک بات آزمایشی است.')

def sms_bomber(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("شماره مورد نظر را وارد کنید:")
    user_data[update.message.chat_id] = 'awaiting_number'

def handle_message(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    text = update.message.text

    if chat_id in user_data and user_data[chat_id] == 'awaiting_number':
        phone_number = text
        user_data[chat_id] = phone_number
        for _ in range(100):
            message_body = f'پیام رندوم شماره {random.randint(1, 1000)}'
            update.message.reply_text(message_body)
        update.message.reply_text("100 پیام به شماره مورد نظر ارسال شد.")
        user_data.pop(chat_id, None)
    else:
        update.message.reply_text("دستور نامعتبر است. لطفا دوباره امتحان کنید.")

def main() -> None:
    updater = Updater(TELEGRAM_BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("sms_bomber", sms_bomber))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
