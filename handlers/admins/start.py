from datetime import datetime
from time import sleep
from keyboards.inline.start_keyboard import start_keyboard
from utils.config import ConfigBot, bot
from telebot import types
from utils.db_api.home_db.handlers import user as users_db
from utils.notification import MyLogger

logger = MyLogger()


@bot.message_handler(
    commands=["start"],
    func=lambda message: str(message.from_user.id) in ConfigBot.admin
    and message.chat.id == message.from_user.id,
)
def bot_start(message: types.Message):
    """Обработка команды /start для админа"""

    user_id = message.from_user.id
    # Отправляем приветсвенное сообщение
    msg = bot.send_message(
        chat_id=message.chat.id,
        text=f"Привет, Админ {message.from_user.full_name}!",
        reply_to_message_id=message.message_id,
    )

    # Проверяем есть ли пользователь в базе
    if user := users_db.get(message.from_user.id):
        # Обновляем имя если оно отличается от текущего
        if user.UserFullName != message.from_user.full_name:
            logger.info(
                f"Пользователь {user.UserId} сменил имя: {user.UserFullName} > {message.from_user.full_name}"
            )
            users_db.update(user.UserId, message.from_user.full_name)
    else:
        # Добавляем нового пользователя
        user = users_db.add(
            UserId=message.from_user.id,
            UserFullName=message.from_user.full_name,
            Status="admin",
            DateStart=datetime.now(),
        )
        logger.new_user(user)

    sleep(2)
    # Изменяем сообщение с меню бота
    bot.edit_message_text(
        "Выбери действие:",
        message.chat.id,
        message_id=msg.message_id,
        reply_markup=start_keyboard(),
    )

