from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()

@router.message(Command('start'))
async def handle_go(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}', reply_markup=kb.menu_reply_markup)
