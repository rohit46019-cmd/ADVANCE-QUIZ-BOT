import logging
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import TELEGRAM_TOKEN, USE_WEBHOOK, WEBHOOK_URL, HOST, PORT
from handlers import (
    start_handler, help_handler, ai_handler, static_handler,
    progress_handler, export_handler, admin_handler
)
from utils.logger import setup_logging

setup_logging()
logger = logging.getLogger("quiz-bot")

def main():
   app = Application.builder().token(TELEGRAM_TOKEN).build()


    # Commands
    app.add_handler(CommandHandler("start", start_handler.start))
    app.add_handler(CommandHandler("help", help_handler.help_command))
    app.add_handler(CommandHandler("ai", ai_handler.ai_quiz))
    app.add_handler(CommandHandler("static", static_handler.static_quiz))
    app.add_handler(CommandHandler("progress", progress_handler.show_progress))
    app.add_handler(CommandHandler("html", export_handler.export_html))
    app.add_handler(CommandHandler("pdf", export_handler.export_pdf))
    app.add_handler(CommandHandler("sque", export_handler.show_saved))
    app.add_handler(CommandHandler("stored", export_handler.show_stored))
    app.add_handler(CommandHandler("setfooter", admin_handler.set_footer))
    app.add_handler(CommandHandler("api", admin_handler.set_api))
    app.add_handler(CommandHandler("hint", ai_handler.hint))

    # Inline buttons for answers and config
    app.add_handler(CallbackQueryHandler(ai_handler.handle_button, pattern="^(A|B|C|D|save|skip|explain)$"))
    app.add_handler(CallbackQueryHandler(ai_handler.handle_config, pattern="^(lang_|diff_|timer_|shuffle_|neg_)"))

    # Capture prompt text after /ai
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ai_handler.capture_prompt))

    # Robust webhook → polling fallback
    if USE_WEBHOOK and WEBHOOK_URL:
        try:
            logger.info(f"Starting webhook on {HOST}:{PORT} -> {WEBHOOK_URL}")
            app.run_webhook(
                listen=HOST,
                port=PORT,                          # If PORT not open/allowed, exception triggers fallback
                url_path="bot",
                webhook_url=WEBHOOK_URL.rstrip("/") + "/bot",
                drop_pending_updates=True,
            )
        except Exception as e:
            logger.error(f"Webhook failed or port not open: {e}. Falling back to polling.")
            app.run_polling(drop_pending_updates=True)
    else:
        logger.info("Polling mode (no open port or webhook not configured).")
        app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
