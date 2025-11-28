import json, os
from cryptography.fernet import Fernet
from config import ENCRYPTION_KEY

DATA_FILE = "data/user_api_keys.json"

def _fernet():
    key = ENCRYPTION_KEY.encode() if isinstance(ENCRYPTION_KEY, str) else ENCRYPTION_KEY
    return Fernet(key)

def save_api_key(user_id, service, api_key):
    data = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    enc = _fernet().encrypt(api_key.encode()).decode()
    data[str(user_id)] = {"service": service, "api_key": enc}
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def get_api_info(user_id):
    if not os.path.exists(DATA_FILE): return None
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    rec = data.get(str(user_id))
    if not rec: return None
    api_key = _fernet().decrypt(rec["api_key"].encode()).decode()
    return {"service": rec["service"], "api_key": api_key}
