from telebot import types
from utils.config import ConfigBot, bot
import time


CONTENT_TYPES = [
    "text",
    "audio",
    "document",
    "photo",
    "sticker",
    "video",
    "video_note",
    "voice",
    "location",
    "contact",
    "new_chat_members",
    "left_chat_member",
    "new_chat_title",
    "new_chat_photo",
    "delete_chat_photo",
    "group_chat_created",
    "supergroup_chat_created",
    "channel_chat_created",
    "migrate_to_chat_id",
    "migrate_from_chat_id",
    "pinned_message",
]


@bot.message_handler(
    content_types=CONTENT_TYPES,
    func=lambda message: str(message.from_user.id) in ConfigBot.admin
    and not message.via_bot,
)
def bot_text(message: types.Message):
    tconv = lambda x: time.strftime(
        "%H:%M:%S %d.%m.%Y", time.localtime(x)
    )  # Конвертация даты в читабельный вид

    if message.forward_date:
        if message.forward_from:
            user_id = f"`{message.forward_from.id}`"
            user_name = f"`{message.forward_from.first_name}`"
        else:
            user_id = "Неудалось получить"
            user_name = f"`{message.forward_sender_name}`"

        info_message = "\n".join(
            [
                f"Пересланное сообщение:",
                f"**ID пользователя:** {user_id}",
                f"**Имя пользователя:** {user_name}",
                f"**Дата отправки:** `{tconv(message.forward_date)}`",
            ]
        )
    else:
        info_message = "\n".join(
            [
                f"**ID сообщения:** `{message.message_id}`",
                f"**ID чата:** `{message.chat.id}`",
                f"**ID пользователя:** `{message.from_user.id}`",
                f"**Текст сообщения: `{message.text}`",
                f"**Дата отправки:** `{tconv(message.date)}`",
            ]
        )

    bot.send_message(
        message.chat.id,
        info_message,
        parse_mode="Markdown",
    )
