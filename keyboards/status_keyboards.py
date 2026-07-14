from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def status_keyboards():
    buttons=[
        [InlineKeyboardButton(text="Живой", callback_data="alive"),
         InlineKeyboardButton(text="Неизвестно", callback_data="unknown"),
         InlineKeyboardButton(text="Мертвый", callback_data="dead")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)