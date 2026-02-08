import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

TOKEN = "8423480524:AAH8OV6vzRX6J9jc2kn-vyGUjboJurUt9z8"

async def start_cmd(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="▶️ Запустити гру",
                web_app=WebAppInfo(
                    url="https://Wed/index.html"
                )
            )
        ]
    ])
    await message.answer(
        "Натисни кнопку, щоб відкрити гру 👇",
        reply_markup=keyboard
    )

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.message.register(start_cmd, Command("start"))

    await dp.start_polling(bot)

    asyncio.run(main())