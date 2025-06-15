from aiogram import Bot, Dispatcher

import os
import logging
import asyncio
from dotenv import load_dotenv, find_dotenv

from handlers import handler_test

load_dotenv(find_dotenv())

async def main():
    bot = Bot(token=os.getenv('TOKEN'))  
    dp = Dispatcher()  
    dp.include_router(handler_test.router)  
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)  


if __name__ == "__main__":
    #Логирование лучше убрать так как треубет много ресурсов в продакшене
    logging.basicConfig(level=logging.INFO) 
    asyncio.run(main())  