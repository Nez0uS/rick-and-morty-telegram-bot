import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import Config

from handlers.handler import start_router
from handlers.random_charachter import random_character_router as random_character
from handlers.search_by_name import search_by_name_router as search_by_name
from handlers.search_by_status import search_by_status_router as search_by_status



async def main():
    config = Config()
    bot = Bot(config.TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(start_router)
    dp.include_router(random_character)
    dp.include_router(search_by_name)
    dp.include_router(search_by_status)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())