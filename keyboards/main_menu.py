from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():
    buttons=[
        [InlineKeyboardButton(text="Случайный персонаж", callback_data="random")],
        [InlineKeyboardButton(text="Найти персонажа по имени", callback_data="search_by_name")],
        [InlineKeyboardButton(text="Найти персонажа по статусу", callback_data="search_by_status")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)



