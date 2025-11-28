from telegram import Update
from telegram.ext import ContextTypes
from models.quiz_session import SessionManager
from models.question import Question
from utils.buttons import answer_buttons

async def static_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if SessionManager.has_active(user_id):
        await update.message.reply_text("⛔ Active quiz in progress. Finish it first.")
        return

    # Demo static questions; production: parse HTML/PDF/manual
    questions = [
        Question(1, "2 + 2 = ?", {"A":"3","B":"4","C":"5","D":"22"}, "B", "Because 2+2=4"),
        Question(2, "Capital of India?", {"A":"Mumbai","B":"Kolkata","C":"New Delhi","D":"Hyderabad"}, "C", "Constitutional capital"),
    ]
    session = SessionManager.start(user_id, mode="static")
    session.load_questions(questions)
    q = session.current_question()
    await update.message.reply_text(
        f"Q{q.serial}. {q.to_dict()['question']} 🧩",
        reply_markup=answer_buttons()
    )
