from telegram import Update
from telegram.ext import ContextTypes

HELP = (
    "📖 Commands:\n"
    "/start - Start bot\n"
    "/help - Show help\n"
    "/ai - Start AI quiz (prompt-based)\n"
    "/static - Start static quiz (HTML/PDF/manual)\n"
    "/hint - AI hint for current question\n"
    "/progress - Show progress checkpoint\n"
    "/html - Export current quiz to HTML\n"
    "/pdf - Export current quiz to PDF\n"
    "/sque - Show saved questions\n"
    "/stored - Show stored quizzes\n"
    "/setfooter - Admin: set footer message\n"
    "/api - Set your AI API key (Gemini/OpenAI/Perplexity)"
)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP)
