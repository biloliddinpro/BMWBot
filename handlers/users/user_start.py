from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.user import phone_number
from states.user import RegisterState
from loader import dp
from aiogram.dispatcher import FSMContext
from utils.db_api.user_commands import *
from keyboards.default.user import *


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if await get_user(
            chat_id=message.chat.id):
        text = "Assalomu alaykum, xush kelibsiz."
        await message.answer(text=text, reply_markup=bmw_main_menu)
    else:
        text = "Iltimos o'zingizni Ismingizni kiriting"
        await message.answer(text=text)
        await RegisterState.full_name.set()


@dp.message_handler(state=RegisterState.full_name)
async def f_handler(message: types.Message, state: FSMContext):
    text = "Telefon raqamingizni kiriting"
    await message.answer(text=text, reply_markup=phone_number)
    await state.update_data(full_name=message.text)
    await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number, content_types=types.ContentType.CONTACT)
async def phone_handler(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number, chat_id=message.chat.id, created_at=message.date)
    data = await state.get_data()
    user = await add_user(data=data)
    if user:
        text = "🥳 Siz muvafaqqiyatli ro'yxatdan o'tdingiz."
    else:
        text = "Botda moummo bor emish"
    await message.answer(text=text, reply_markup=bmw_main_menu)
    await state.finish()