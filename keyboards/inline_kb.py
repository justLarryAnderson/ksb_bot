from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

user_data = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Введите ФИО', callback_data='full_name')],
        [InlineKeyboardButton(text='Наименование образовательной организации', callback_data='university')]
    ]
)

