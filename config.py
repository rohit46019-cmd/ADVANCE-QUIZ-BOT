import os

# Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")

# Webhook settings (Render-friendly)
USE_WEBHOOK = os.getenv("USE_WEBHOOK", "false").lower() == "true"
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "")  # e.g., https://your-app.onrender.com/bot
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "10000"))  # Render injects PORT

# Encryption key for Fernet (base64 32-byte). Generate once and set as env.
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY", "BASE64_FERNET_KEY")

# Admin
ADMIN_IDS = [int(x) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip().isdigit()]
FOOTER_FILE = "data/footer.txt"

# Defaults
DEFAULT_TOTAL_QUESTIONS = 10
DEFAULT_TIMER_SECONDS = 15
DEFAULT_NEGATIVE_MARKING = 0.0
