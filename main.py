import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router


async def main():
    bot = Bot(token='7907066022:AAHNS5S51MnqtAtEII59m5W3cUwh9faKre8')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    print('Бот запущен')
    asyncio.run(main())
