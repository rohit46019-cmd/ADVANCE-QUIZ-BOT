from telegram import Update
from telegram.ext import ContextTypes
from models.quiz_session import SessionManager
from utils.progress_bar import generate_progress_bar

async def show_progress(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    session = SessionManager.get(user_id)
    if not session or not session.active:
        await update.message.reply_text("⚠️ No active quiz.")
        return
    bar = generate_progress_bar(session.stats["attempted"], session.total)
    acc = (session.stats["correct"] / max(1, session.stats["attempted"])) * 100
    await update.message.reply_text(
        f"📊 Progress:\n"
        f"Attempted: {session.stats['attempted']}\n"
        f"Correct: {session.stats['correct']}\n"
        f"Wrong: {session.stats['wrong']}\n"
        f"Skipped: {session.stats['skipped']}\n"
        f"Saved: {session.stats['saved']}\n"
        f"Accuracy: {acc:.2f}%\n"
        f"{bar}"
    )
