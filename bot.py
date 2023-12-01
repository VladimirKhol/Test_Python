import logging
import settings
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

USER_NAME = 'lets_do_python_bot'
CHAT_NAME = 'Learn Python Now'


logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                    level=logging.INFO,
                    filename='bot.log',
                    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    welcometext = rf"""Привіт {user.mention_html()} ❤️,
Чим я можу тобі допомогти?"""
    await update.message.reply_html(
        welcometext,
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Що саме тебе цікавить?")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)


def main() -> None:
    application = Application.builder().token(settings.BOT_KEY).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    logging.info('Bot started')
    main()


