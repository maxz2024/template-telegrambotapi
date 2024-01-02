from utils.config import bot
from loguru import logger
import handlers
from utils.notification import MyLogger
    
def main():
    
    logger.info(f"Запущен бот: {bot.get_me().username}")
    # MyLogger().start()
    bot.infinity_polling(skip_pending=True, timeout=200)

if __name__ == "__main__":
    main()
