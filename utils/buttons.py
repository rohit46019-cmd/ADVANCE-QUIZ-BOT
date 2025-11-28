from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def answer_buttons():
    keyboard = [
        # First row → 3 buttons
        [
            InlineKeyboardButton("A", callback_data="A"),
            InlineKeyboardButton("B", callback_data="B"),
            InlineKeyboardButton("C", callback_data="C"),
        ],
        # Second row → 2 buttons
        [
            InlineKeyboardButton("D", callback_data="D"),
            InlineKeyboardButton("⭐ Save", callback_data="save"),
        ],
        # Third row → 3 buttons
        [
            InlineKeyboardButton("↩ Skip", callback_data="skip"),
            InlineKeyboardButton("⚡ Explanation", callback_data="explain"),
            InlineKeyboardButton("❓ Hint", callback_data="hint"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def config_buttons():
    keyboard = [
        # First row → 3 buttons
        [
            InlineKeyboardButton("English", callback_data="lang_en"),
            InlineKeyboardButton("Hindi", callback_data="lang_hi"),
            InlineKeyboardButton("Bilingual", callback_data="lang_bi"),
        ],
        # Second row → 2 buttons
        [
            InlineKeyboardButton("Easy", callback_data="diff_easy"),
            InlineKeyboardButton("Moderate", callback_data="diff_mod"),
        ],
        # Third row → 3 buttons
        [
            InlineKeyboardButton("Hard", callback_data="diff_hard"),
            InlineKeyboardButton("Most Hard", callback_data="diff_mhard"),
            InlineKeyboardButton("10s", callback_data="timer_10"),
        ],
        # Fourth row → 2 buttons
        [
            InlineKeyboardButton("15s", callback_data="timer_15"),
            InlineKeyboardButton("20s", callback_data="timer_20"),
        ],
        # Fifth row → 3 buttons
        [
            InlineKeyboardButton("25s", callback_data="timer_25"),
            InlineKeyboardButton("Shuffle Yes", callback_data="shuffle_yes"),
            InlineKeyboardButton("Shuffle No", callback_data="shuffle_no"),
        ],
        # Sixth row → 2 buttons
        [
            InlineKeyboardButton("Neg On", callback_data="neg_on"),
            InlineKeyboardButton("Neg Off", callback_data="neg_off"),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
