def generate_progress_bar(current, total):
    slots = 5
    filled = max(0, min(slots, int((current / max(1, total)) * slots)))
    return "[" + "▓" * filled + "░" * (slots - filled) + "]"
