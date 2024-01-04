from telebot.handler_backends import State, StatesGroup


class Template(StatesGroup):
    message_id = State()
