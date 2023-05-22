from typing import Final
from telegram import Update
from telegram.ext import ContextTypes, Application, CommandHandler, MessageHandler, filters
import gpt

TOKEN: Final = 'TELEGRAM_BOT_KEY'
BOT_USERNAME: Final = 'TELEGRAM_BOT_USERNAME'


async def start_command(update: Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to The Nirvana AI chat!")


async def help_command(update: Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a AI based customer service created by The Nirvana")



def handle_response(update: Update) -> str:
    
    response = gpt.askGPT(update)

    return response

async def handle_message(update: Update, context : ContextTypes.DEFAULT_TYPE):
    response: str = handle_response(update)

    await update.message.reply_text(response)


async def error(update: Update, context : ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))

    app.add_handler(CommandHandler('help', help_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    app.run_polling(poll_interval=3)
