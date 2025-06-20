from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

confirm_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Подтвердить данные', callback_data='confirm_data')],
        [InlineKeyboardButton(text='Нашел ошибку', callback_data='change_data')]
    ]
)


