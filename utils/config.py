import configparser
import json
from pathlib import Path
from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from telebot import custom_filters

class Configurate:
    """Класс конфигурации"""

    def __init__(self):
        self.path_config: str = Path("files/config.ini")
        if not self.path_config.exists():
            if not (path_files := Path("files")).exists():
                path_files.mkdir()
            self.create()

        self.config = self.read()

    def create(self):
        """Создание конфигурации"""

        # bot
        token = input("Введите токен бота: ")
        admin = input("Ввведите id администратора: ")

        config = configparser.ConfigParser()

        config["bot"] = {"token": token, "admin": admin}

        config["settings"] = {
            "chat_id": "None",
            "channel_id": "None",
            "channel_url": "None",
            "topic_notification": "None",
            "topic_users": "None",
        }

        self.config = config
        self.save()

    def save(self):
        """Сохранение конфигурации"""

        with open(self.path_config, "w", encoding="utf-8") as configfile:
            self.config.write(configfile)

    def read(self):
        """Чтение конфигурации"""

        config = configparser.ConfigParser()
        config.read(self.path_config, encoding="utf-8")
        return config

    def edit(self, name_settings: str, parameter: str, value: str | int):
        """Редактирование конфигурации"""

        self.config[name_settings][parameter] = str(value)
        self.save()


config = Configurate().config


class ConfigBot:
    token = config["bot"]["token"]
    admin = config["bot"]["admin"]


class ConfigSettings:
    chat_id = config["settings"]["chat_id"]
    channel_id = config["settings"]["channel_id"]
    channel_url = config["settings"]["channel_url"]
    topic_notification = config["settings"]["topic_notification"]
    topic_users = config["settings"]["topic_users"]

state_storage = StateMemoryStorage()
bot = TeleBot(ConfigBot.token, state_storage=state_storage)
bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())