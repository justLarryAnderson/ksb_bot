from aiogram.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup

delite_kb = ReplyKeyboardRemove()

registration_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Хочу зарегестрироваться')],
        [KeyboardButton(text='Изменить данные')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Введите свое ФИО и название образовательной организации полностью'
)

