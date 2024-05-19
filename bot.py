import asyncio
import logging
import coloredlogs

from aiogram import Bot, Dispatcher
from config import BOT

from handlers import router

coloredlogs.install(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = BOT["token"]


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=BOT["parse_mode"])
    logger.info("Bot started")
    try:
        disp = Dispatcher()
        disp.include_router(router)
        await disp.start_polling(bot)
    except Exception as e:
        logger.error(e)
    finally:
        logger.info("Bot stopped")
        # await bot.close()
        pass


asyncio.run(main())
