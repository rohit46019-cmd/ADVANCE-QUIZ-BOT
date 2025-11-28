import os
from config import FOOTER_FILE

def get_footer():
    if os.path.exists(FOOTER_FILE):
        with open(FOOTER_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    return "© Ultra Advanced Quiz Bot"
