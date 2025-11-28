from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_IDS, FOOTER_FILE
from services.api_manager import save_api_key

async def set_footer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("⛔ Admin only.")
        return
    text = " ".join(context.args).strip()
    if not text:
        await update.message.reply_text("Usage: /setfooter <message>")
        return
    with open(FOOTER_FILE, "w", encoding="utf-8") as f:
        f.write(text)
    await update.message.reply_text("✅ Footer updated.")

async def set_api(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("Usage: /api <service> <api_key>")
        return
    service, api_key = context.args[0], context.args[1]
    user_id = update.effective_user.id
    save_api_key(user_id, service, api_key)
    await update.message.reply_text("🔑 API key saved securely.")
