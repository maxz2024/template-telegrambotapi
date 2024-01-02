from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_keyboard():
    reply_markup = InlineKeyboardMarkup(row_width=1)
    menu_button = InlineKeyboardButton("Меню", callback_data="menu_button")
    reply_markup.add(menu_button)

    return reply_markup
