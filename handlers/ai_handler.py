from telegram import Update
from telegram.ext import ContextTypes
from utils.buttons import answer_buttons, config_buttons
from utils.progress_bar import generate_progress_bar
from utils.validators import parse_config_callback
from models.quiz_session import SessionManager
from services.ai_generator import generate_questions_for_prompt
from services.api_manager import get_api_info

async def ai_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if SessionManager.has_active(user_id):
        await update.message.reply_text("⛔ You already have an active quiz. Finish it first.")
        return
    session = SessionManager.start(user_id, mode="ai")
    session.state = "awaiting_prompt"
    await update.message.reply_text("🧠 Send your topic/prompt (e.g., 'Data Structures MCQ - Trees & Graphs').")

async def capture_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    session = SessionManager.get(user_id)
    if not session or session.state != "awaiting_prompt":
        return
    session.prompt = update.message.text.strip()
    session.state = "configuring"
    await update.message.reply_text("⚙️ Choose your quiz settings:", reply_markup=config_buttons())

async def handle_config(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    session = SessionManager.get(user_id)
    if not session or session.state not in ("configuring", "awaiting_prompt"):
        await query.edit_message_text("⚠️ No active session. Use /ai to start.")
        return

    field, value = parse_config_callback(query.data)
    session.config[field] = value
    await query.message.reply_text(f"✅ Set {field} to {value}")

    # When config is ready, generate questions
    if session.is_config_ready():
        api = get_api_info(user_id)
        if not api:
            await query.message.reply_text("🔑 Set API key first: /api <service> <api_key>")
            return
        await query.message.reply_text("🤖 Generating questions...")
        qlist = generate_questions_for_prompt(session.prompt, session.config, api)
        session.load_questions(qlist)
        q = session.current_question()
        await query.message.reply_text(
            f"Q{q.serial}. {q.to_dict()['question']} 🧩",
            reply_markup=answer_buttons()
        )
        session.state = "in_quiz"

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    session = SessionManager.get(user_id)
    if not session or not session.active:
        await query.edit_message_text("⚠️ No active session. Use /ai or /static to start.")
        return

    q = session.current_question()
    data = query.data

    if data in ["A", "B", "C", "D"]:
        session.stats["attempted"] += 1
        if data == q.answer:
            session.stats["correct"] += 1
            await query.edit_message_text(f"✅ Correct! {data}")
        else:
            session.stats["wrong"] += 1
            await query.edit_message_text(f"❌ Wrong. You chose {data}")

        # checkpoint
        if session.stats["attempted"] % 10 == 0:
            bar = generate_progress_bar(session.stats["attempted"], session.total)
            acc = (session.stats["correct"] / max(1, session.stats["attempted"])) * 100
            await query.message.reply_text(
                f"📊 Checkpoint:\n"
                f"Attempted: {session.stats['attempted']}\n"
                f"Correct: {session.stats['correct']}\n"
                f"Wrong: {session.stats['wrong']}\n"
                f"Skipped: {session.stats['skipped']}\n"
                f"Saved: {session.stats['saved']}\n"
                f"Accuracy: {acc:.2f}%\n"
                f"{bar}"
            )

        # next or end
        if session.next():
            nq = session.current_question()
            await query.message.reply_text(
                f"Q{nq.serial}. {nq.to_dict()['question']} 🧩",
                reply_markup=answer_buttons()
            )
        else:
            await end_quiz_summary(query, session)

    elif data == "save":
        session.stats["saved"] += 1
        SessionManager.save_current(user_id)
        await query.edit_message_text("⭐ Saved for later.")

    elif data == "skip":
        session.stats["skipped"] += 1
        await query.edit_message_text("↩ Skipped.")
        if session.next():
            nq = session.current_question()
            await query.message.reply_text(
                f"Q{nq.serial}. {nq.to_dict()['question']} 🧩",
                reply_markup=answer_buttons()
            )
        else:
            await end_quiz_summary(query, session)

    elif data == "explain":
        await query.message.reply_text(f"⚡ Explanation: {q.explanation}")

async def hint(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    session = SessionManager.get(user_id)
    if not session or not session.active:
        await update.message.reply_text("⚠️ No active session.")
        return
    await update.message.reply_text("💡 Hint: Focus on the key terms and eliminate distractors.")

async def end_quiz_summary(query, session):
    neg = session.config.get("negative_marking", 0.0)
    marks = session.stats["correct"] - (session.stats["wrong"] * neg)
    acc = (session.stats["correct"] / max(1, session.stats["attempted"])) * 100
    await query.message.reply_text(
        "🏁 Quiz Finished!\n"
        f"Total: {session.total}\n"
        f"Correct: {session.stats['correct']}\n"
        f"Wrong: {session.stats['wrong']}\n"
        f"Skipped: {session.stats['skipped']}\n"
        f"Saved: {session.stats['saved']}\n"
        f"Accuracy: {acc:.2f}%\n"
        f"Marks: {marks:.2f}\n"
        f"Time: {session.elapsed_time():.1f}s"
    )
    SessionManager.end(session.user_id)
