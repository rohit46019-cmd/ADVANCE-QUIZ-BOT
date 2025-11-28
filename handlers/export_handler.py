from telegram import Update
from telegram.ext import ContextTypes
from models.quiz_session import SessionManager
from services.html_exporter import export_html_file
from services.pdf_exporter import export_pdf_file
from models.storage import Storage

async def export_html(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    session = SessionManager.get(user_id)
    if not session:
        await update.message.reply_text("⚠️ No active session.")
        return
    path = export_html_file(session)
    await update.message.reply_text(f"📝 Exported HTML: {path}")

async def export_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    session = SessionManager.get(user_id)
    if not session:
        await update.message.reply_text("⚠️ No active session.")
        return
    path = export_pdf_file(session)
    await update.message.reply_text(f"📄 Exported PDF: {path}")

async def show_saved(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    saved = Storage.get_saved(user_id)
    if not saved:
        await update.message.reply_text("⭐ No saved questions yet.")
        return
    text = "⭐ Saved Questions:\n" + "\n".join([f"Q{q['serial']}: {q['question']}" for q in saved[:25]])
    await update.message.reply_text(text)

async def show_stored(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quizzes = Storage.get_stored_quizzes()
    if not quizzes:
        await update.message.reply_text("📦 No stored quizzes.")
        return
    await update.message.reply_text("📦 Stored quizzes available (demo).")
