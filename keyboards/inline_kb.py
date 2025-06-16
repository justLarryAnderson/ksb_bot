from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

confirm_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Проверил, подтвердить данные', callback_data='confirm_data')],
        [InlineKeyboardButton(text='Кажется нашел ошибку, исправлю', callback_data='change_data')]
    ]
)


