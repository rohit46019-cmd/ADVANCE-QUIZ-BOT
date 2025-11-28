# Ultra Advanced Interactive Quiz Bot

A feature-rich Telegram bot that delivers interactive quizzes in multiple modes with AI integration, progress tracking, and export options.

---

## 🚀 Features

- **Quiz Modes**
  - 🤖 AI Quiz (Gemini/OpenAI/Perplexity powered)
  - 📄 Static Quiz (HTML/PDF/manual input)
  - ⚔️ Duel Mode (two users compete head-to-head)
  - 🏆 Tournament Mode (multi-user competition with leaderboard)
  - 📚 Story Mode (chapter-based quizzes with checkpoints)
  - 🎙️ Voice Quiz (questions read aloud, answered via buttons)
  - 🖼️ Image Quiz (questions with images)

- **User Interaction**
  - Inline buttons: **A/B/C/D**, ⭐ Save, ↩ Skip, ⚡ Explanation
  - Pre-quiz configuration: language, difficulty, timer, shuffle, negative marking
  - Emoji support in questions, answers, explanations, and progress bars

- **Progress Tracking**
  - Checkpoints every 10 questions
  - Visual progress bar `[▓▓▓░░░]`
  - Accuracy %, attempted, correct, wrong, skipped, saved stats

- **End-of-Quiz Summary**
  - Total questions
  - Correct, wrong, skipped, saved
  - Accuracy %
  - Marks (with optional negative marking)
  - Total time taken

- **Admin & Anti-Spam**
  - Prevents multiple quizzes at the same time
  - Admin can set mandatory footer/credit message
  - Footer shown in welcome and optionally at quiz end

- **Save & Export**
  - ⭐ Save questions mid-quiz
  - 📄 Export quizzes to HTML or PDF
  - View saved questions and stored quizzes

- **AI Integration**
  - Users provide their own API keys (Gemini/OpenAI/Perplexity)
  - Keys stored securely (encrypted)
  - Dynamic question generation based on user prompt

- **Deployment**
  - Works with webhook or polling
  - ✅ Auto-fallback to polling if **no open port detected**

---

## 📖 Commands

| Command        | Description |
|----------------|-------------|
| `/start`       | Start bot, greet user, show footer |
| `/help`        | Show all commands with explanations |
| `/ai`          | Start AI-generated quiz using user prompt |
| `/static`      | Start static quiz from HTML/PDF/manual |
| `/duel`        | Start duel quiz between two users |
| `/tournament`  | Start tournament quiz with leaderboard |
| `/story`       | Start story/chapter-based quiz |
| `/voicequiz`   | Start voice-based quiz |
| `/imgquiz`     | Start image-based quiz |
| `/hint`        | Provide AI-generated hint for current question |
| `/progress`    | Show progress checkpoint (stats + progress bar) |
| `/html`        | Export current quiz to HTML |
| `/pdf`         | Export current quiz to PDF |
| `/sque`        | Show saved questions |
| `/stored`      | Show stored quizzes |
| `/setfooter`   | Admin command to set footer/credit message |
| `/api`         | User sets their personal AI API key |

---

## ⚙️ Setup

1. Create virtual environment and install dependencies:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt


   Set environment variables:

   export TELEGRAM_TOKEN=your_bot_token
export ENCRYPTION_KEY=$(python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())")
export ADMIN_IDS=123456789
export USE_WEBHOOK=false

Run locally:
python bot.py


