from time import sleep
from utils.config import ConfigSettings, bot
from utils.db_api.home_db.models.user import User
from telebot import types
from loguru import logger


class MyLogger:
    def __init__(self) -> None:
        pass

    def start(self):
        # msg = bot.send_message(
        #     ConfigSettings.chat_id,
        #     "Бот запущен.",
        #     reply_to_message_id=ConfigSettings.topic_notification,
        #     disable_notification=True,
        # )
        # sleep(10)
        # bot.delete_message(ConfigSettings.chat_id, msg.message_id)
        logger.info("Бот запущен.")

    def info(self, text):
        # bot.send_message(
        #     ConfigSettings.chat_id,
        #     text,
        #     reply_to_message_id=ConfigSettings.topic_notification,
        #     disable_notification=True,
        # )
        logger.info(text)

    def new_user(self, user: User):
        text = "\n".join(
            [
                f"Новый пользователь.",
                f"Имя:  `{user.UserFullName}`",
                f"Id:  `{user.UserId}`",
                f"Статус:  `{user.Status}`",
                f"Время авторизации:  `{user.DateStart.strftime('%H:%M %m.%d.%Y')}`",
            ]
        )

        # msg = bot.send_message(
        #     ConfigSettings.chat_id,
        #     text,
        #     reply_to_message_id=ConfigSettings.topic_users,
        #     parse_mode="Markdown",
        #     reply_markup=types.InlineKeyboardMarkup().add(
        #         types.InlineKeyboardButton(
        #             "Профиль пользователя", url=f"tg://user?id={user.UserId}"
        #         )
        #     ),
        # )
        logger.info(text)

    def debug(self, text):
        # msg = bot.send_message(
        #     ConfigSettings.chat_id,
        #     text,
        #     reply_to_message_id=ConfigSettings.topic_notification,
        #     disable_notification=False,
        # )
        logger.debug(text)
