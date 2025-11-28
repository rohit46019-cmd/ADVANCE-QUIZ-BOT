from telegram import Update
from telegram.ext import ContextTypes
from utils.common import get_footer
from models.quiz_session import SessionManager

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    SessionManager.ensure_user(update.effective_user.id)
    footer = get_footer()
    await update.message.reply_text(
        "👋 Welcome to Ultra Advanced Quiz Bot!\n"
        "Use /help to see all commands.\n"
        f"{footer}"
    )
