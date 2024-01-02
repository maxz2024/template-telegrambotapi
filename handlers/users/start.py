import pprint
from time import sleep
from keyboards.inline.start_keyboard import start_keyboard
from utils.notification import MyLogger
from utils.config import bot, ConfigBot, ConfigSettings
from telebot import types
from utils.db_api.home_db.handlers import user as users_db
from datetime import datetime


logger = MyLogger()


@bot.message_handler(
    commands=["start"], func=lambda message: message.chat.id == message.from_user.id
)
def bot_start(message: types.Message):
    """Обработка команды /start"""

    user_id = message.from_user.id
    # Отправляем приветсвенное сообщение
    msg = bot.send_message(
        chat_id=user_id,
        text=f"Привет, {message.from_user.full_name}!",
        reply_to_message_id=message.message_id,
    )

    # Проверяем подписку на канал
    # if bot.get_chat_member(ConfigSettings.channel_id, user_id).status in [
    #     "left",
    #     "kicked",
    # ]:
    #     # Отправляем приглашение в канал
    #     bot.send_message(
    #         user_id,
    #         "Для доступа к боту, подпишитесь на канал. Приму всех когда бот будет работать.",
    #         reply_markup=types.InlineKeyboardMarkup(row_width=1).add(
    #             types.InlineKeyboardButton(
    #                 "Подписаться 👌",
    #                 url=f"tg://join?invite={ConfigSettings.channel_url}",
    #             ),
    #             types.InlineKeyboardButton(
    #                 "Проверить ✅", callback_data="check_member_channel_button"
    #             ),
    #         ),
    #     )
    #     return
    
    # Проверяем есть ли пользователь в базе
    if user := users_db.get(message.from_user.id):
        # Проверяем статус пользователя на ban
        if user.Status == "ban":
            # Отправляем сообщение о блокировке и завершаем функцию
            bot.send_message(
                user.UserId,
                "Ваш статус: заблокирован. Причину можете узанть у админа.",
                reply_markup=types.InlineKeyboardMarkup().add(
                    types.InlineKeyboardButton(
                        "Чат администратора.", url=f"tg://user?id={ConfigBot.admin}"
                    )
                ),
            )
            return
        else:
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


# @bot.callback_query_handler(
#     func=lambda callback_query: callback_query.data == "check_member_channel_button"
# )
# def check_member_channel(callback_query: types.CallbackQuery):
#     if bot.get_chat_member(
#         ConfigSettings.channel_id, callback_query.from_user.id
#     ).status not in ["left", "kicked"]:
#         msg = bot.send_message(
#             callback_query.from_user.id,
#             "Спасибо за подпсику. Обязательно ознакомся с правилами бота в канале.",
#         )
#     else:
#         bot.answer_callback_query(callback_query.id, "Вы не подписались.")
#         return

#     sleep(3)
#     bot.edit_message_text(
#         "Выбери действие:",
#         callback_query.from_user.id,
#         message_id=callback_query.message.message_id,
#         reply_markup=start_keyboard(),
#     )
#     bot.delete_message(callback_query.from_user.id, msg.message_id)
