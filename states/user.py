from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup

class RegisterState(StatesGroup):
    full_name = State()
    phone_number = State()