import asyncio
from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.filters import Command
from aiogram import F, Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from keyboards import inline_kb, reply_kb
from database.db import Database


class Registration(StatesGroup):
#Поля регистрации пользователя
    name = State()
    university = State()

user_router = Router()

@user_router.message(Command('start'))
async def start_command(message: Message):
    await message.answer(
        text='Тогда начинаем!🎉Сначало нужн пройти регистрацию(кнопка винизу), где нужно указать свое ФИО и наименование образовательной организации полностью🏫.',
        reply_markup=reply_kb.registration_keyboard
        )

@user_router.message(F.text == 'Зарегестрироваться')
async def registration(message: Message, state: FSMContext):
    await state.set_state(Registration.name)
    await message.answer(text='Введите свое ФИО через пробел.')

#Состояния регистрации
@user_router.message(Registration.name)
async def registr_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registration.university)
    await message.answer(text='Введите название вашего образовательного учреждения полностью.')
    
@user_router.message(Registration.university)
async def registr_university(message:Message, state: FSMContext):
    await state.update_data(university=message.text)
    data = await state.get_data()
    await message.answer(
        text = f"Вас зовут: {data['name']}\nВаше учебное заведение: {data['university']}.\nХотите изменить данные?",
        reply_markup=inline_kb.confirm_kb
        )    

#Это кастыль говрит Женя как исправить я не ебу. Надо как-то не очищаь сотсоят
@user_router.callback_query(F.data == 'change_data')
async def change_user_data(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Registration.name)
    await callback.answer('Введите данные еще раз')
    await callback.message.answer(text='Введите свое ФИО через пробел.')
#Отправка данных на сервер Postgre
@user_router.callback_query(F.data == 'confirm_data')
async def confirm_user_data(callback: CallbackQuery, state: FSMContext):
    await callback.answer('Данные отправлены')
    #    
    data = await state.get_data()
    await callback.message.answer('Суппер, ваши данные отправлены')
    database = Database()
    asyncio.run(database.insert_user_value(
        name=data['name'],
        university=data['university']))
    state.clear()