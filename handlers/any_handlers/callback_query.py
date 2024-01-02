from loguru import logger
from utils.config import bot 
from telebot import types
from utils.db_api.home_db.handlers import user as users_db

@bot.callback_query_handler(func=lambda callback_query: users_db.get(callback_query.from_user.id) and users_db.get(callback_query.from_user.id).Status != "ban")
def all_callback_query(callback_query: types.CallbackQuery):
    bot.answer_callback_query(callback_query.id, "Ошибка!")
    logger.warning(f"Не обработанный CallbackQuery: {callback_query.data}")