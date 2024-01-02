from utils.config import bot
from telebot import types


@bot.message_handler(
    commands=["help"], func=lambda message: message.chat.id == message.from_user.id
)
def bot_help(message: types.Message):
    text = ("Список команд: ", "/start - Начать диалог", "/help - Получить справку")

    bot.reply_to(message=message, text="\n".join(text))
