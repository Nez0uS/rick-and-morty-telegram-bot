from aiogram import F, Router
from aiogram.types import CallbackQuery

from api import Rick_And_Morty
from keyboards.main_menu import main_menu


router = Router()
api = Rick_And_Morty()

@router.callback_query(F.data == "random")
async def random_character(callback_query: CallbackQuery):
    await callback_query.answer()
    character = await api.get_random_character()
    text = (f"Имя: {character['name']}\n"
            f"Пол: {character['gender']}\n"
            f"Статус: {character['status']}\n\n"
            f"Нажмите, что хотите узнать:"
    )
    await callback_query.message.answer_photo(
        photo=character['image'],
        caption=text,
        reply_markup=main_menu()
    )
