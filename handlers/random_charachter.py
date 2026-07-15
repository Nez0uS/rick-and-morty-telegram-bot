from aiogram import F, Router
from aiogram.types import CallbackQuery

from services.rick_and_morty_api import RickAndMortyAPI
from keyboards.main_menu import main_menu


random_character_router = Router()
api = RickAndMortyAPI()

@random_character_router.callback_query(F.data == "random")
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

    await callback_query.message.delete()
