from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.user import channel_url_keyboard
from loader import dp
from utils.db_api.user_commands import get_user
from utils.cheker import check


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
        text = "Assalomu alaykum, xush kelibsiz."
        await message.answer(text=text)
        text = "Kanalga podpiska tasha"
        await message.answer(text=text, reply_markup=channel_url_keyboard)