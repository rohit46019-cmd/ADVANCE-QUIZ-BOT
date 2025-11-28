from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def answer_buttons():
    keyboard = [
        [InlineKeyboardButton("A", callback_data="A"), InlineKeyboardButton("B", callback_data="B")],
        [InlineKeyboardButton("C", callback_data="C"), InlineKeyboardButton("D", callback_data="D")],
        [InlineKeyboardButton("⭐ Save", callback_data="save"),
         InlineKeyboardButton("↩ Skip", callback_data="skip"),
         InlineKeyboardButton("⚡ Explanation", callback_data="explain")]
    ]
    return InlineKeyboardMarkup(keyboard)

def config_buttons():
    keyboard = [
        [InlineKeyboardButton("English", callback_data="lang_en"),
         InlineKeyboardButton("Hindi", callback_data="lang_hi"),
         InlineKeyboardButton("Bilingual", callback_data="lang_bi")],
        [InlineKeyboardButton("Easy", callback_data="diff_easy"),
         InlineKeyboardButton("Moderate", callback_data="diff_mod"),
         InlineKeyboardButton("Hard", callback_data="diff_hard"),
         InlineKeyboardButton("Most Hard", callback_data="diff_mhard")],
        [InlineKeyboardButton("10s", callback_data="timer_10"),
         InlineKeyboardButton("15s", callback_data="timer_15"),
         InlineKeyboardButton("20s", callback_data="timer_20"),
         InlineKeyboardButton("25s", callback_data="timer_25")],
        [InlineKeyboardButton("Shuffle Yes", callback_data="shuffle_yes"),
         InlineKeyboardButton("Shuffle No", callback_data="shuffle_no")],
        [InlineKeyboardButton("Neg On", callback_data="neg_on"),
         InlineKeyboardButton("Neg Off", callback_data="neg_off")]
    ]
    return InlineKeyboardMarkup(keyboard)
