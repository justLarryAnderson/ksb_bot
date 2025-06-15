from aiogram.types import ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

delite_kb = ReplyKeyboardRemove()

start_keyboard = ReplyKeyboardBuilder()
start_keyboard.add(
    KeyboardButton(text='Введите ваше ФИО'),
    KeyboardButton(text='Наименование образовательной организации')
    )
start_keyboard.adjust(1,1)