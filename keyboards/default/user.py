from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

phone_number = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="telefon raqam jonatish",request_contact=True)
        ]
    ]
)


bmw_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="bmw lani korish")
        ]
    ]
)