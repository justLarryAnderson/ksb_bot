from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.filters import Command
from aiogram import F, Router

from keyboards import inline_kb

router = Router()
name = None
university = None
user = f'Тебя зовут {name}\nИ ты учишся в {university}'

@router.message(Command('start'))
async def start_command(message: Message):
    await message.answer(
        text='Тогда начинаем! 🎉 Введи свое ФИО и наименование образовательной организации🏫\n(кнопки внизу).',
        reply_markup=inline_kb.user_data
        )

@router.callback_query(F.data == 'full_name')
async def input_name(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Введите свое имя')
    