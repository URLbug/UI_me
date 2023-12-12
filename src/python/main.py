# Импорт фреймворков и библиотек
import asyncio

from aiogram import Dispatcher

# Импорт файлов
import database.conn

from __init__ import bot
from handler import home, regist_and_login


async def main() -> None:
    dp = Dispatcher()

    dp.include_routers(home.route, regist_and_login.route)

    print('GOAL!')

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())