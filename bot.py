import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

from handlers import other_handlers, user_handlers
from config_data.config import load_config

# Init logger
logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(level=logging.INFO,
                       format='%(filename)s:%(lineno)d #%(levelname)-8s '
                       '[%(asctime)s] - %(name)s - %(message)s')
    logger.info('Starting bot')

    # Configurations
    config = load_config()
    bot = Bot(token=config.tg_bot.token,
              default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()

    # Register routers
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# Start Bot
if __name__ == '__main__':
    asyncio.run(main())
