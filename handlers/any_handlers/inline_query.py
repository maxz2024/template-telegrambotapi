from loguru import logger
from utils.config import bot 
from telebot import types
from utils.db_api.home_db.handlers import user as users_db

@bot.inline_handler(func=lambda inline_query: len(inline_query.query) > 0 and users_db.get(inline_query.from_user.id) and users_db.get(inline_query.from_user.id).Status != "ban")
def all_inline_query(inline_query: types.InlineQuery):
    logger.warning(f"Не обработанный CallbackQuery: {inline_query.query}")
