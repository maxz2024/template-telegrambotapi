from utils.config import Configurate, bot 
from telebot import types

@bot.channel_post_handler(commands=["channel_save"])
def channel_save(message: types.Message):
    if Configurate().read()["settings"]["channel_id"] == "None":
        Configurate().edit("settings", "channel_id", message.chat.id)
        bot.reply_to(message, "Канал сохранён.")
        channel_url = bot.create_chat_invite_link(message.chat.id,"Приглашение из  Бота.",creates_join_request=True).invite_link.split("+")[-1]
        Configurate().edit("settings", "channel_url", channel_url)
    else:
        bot.reply_to(message, "Канал уже сохранён.")
        