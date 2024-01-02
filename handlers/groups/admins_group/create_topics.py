from utils.config import ConfigBot, ConfigSettings, Configurate, bot 
from telebot import types

@bot.message_handler(commands=["create_topics"], func=lambda message: str(message.from_user.id) == ConfigBot.admin)
def create_topics(message: types.Message):
    
    
    if Configurate().read()["settings"]["chat_id"] == "None":
        chat_id = message.chat.id
        Configurate().edit("settings","chat_id",chat_id)
        
        forum_notification = bot.create_forum_topic(chat_id, "Уведомления")
        Configurate().edit("settings", "topic_notification", forum_notification.message_thread_id)
        bot.send_message(chat_id, "Чат уведомлений.", message_thread_id=forum_notification.message_thread_id)
            
        forum_users = bot.create_forum_topic(chat_id, "Пользователи")
        Configurate().edit("settings", "topic_users", forum_users.message_thread_id)
        bot.send_message(chat_id, "Чат пользователей.", reply_to_message_id=forum_users.message_thread_id)
        
    bot.reply_to(message, "Темы созданы.")
        