from aiogram import Bot,Dispatcher
from tg_bot.handlers.handlers import r
import logging
import asyncio
import os

async def main():
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(r)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())