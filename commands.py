# commands.py

from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    """
    Handler for the /start command.
    Sends a welcome message when the user starts the bot.
    """
    user_first_name = update.effective_user.first_name
    welcome_message = f"Hello {user_first_name}, welcome to your Todo Bot!"
    update.message.reply_text(welcome_message)