from aiogram.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup

delite_kb = ReplyKeyboardRemove()

registration_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Зарегестрироваться')],
    ],
    resize_keyboard=True,
    input_field_placeholder='Введите свое ФИО и название образовательной организации полностью'
)

