from aiogram import F, Router
from aiogram.types import CallbackQuery

from services.RickAndMortyAPI import RickAndMortyAPI
from keyboards.main_menu import main_menu
from keyboards.status_keyboards import status_keyboards

search_by_status_router = Router()
api = RickAndMortyAPI()


@search_by_status_router.callback_query(F.data == "search_by_status")
async def status_keyboard(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("Выберите статус персонажа: ", reply_markup=status_keyboards())
    await callback_query.message.delete()

@search_by_status_router.callback_query(F.data.in_(["alive", "unknown", "dead"]))
async def status_keyboard(callback_query: CallbackQuery):
    await callback_query.answer()
    status = callback_query.data
    result = await api.search_by_status(status)

    text = (f"Имя: {result['name']}\n\n"
            f"Статус: {result['status']}\n"
            f"Пол: {result['gender']}\n\n"
            f"Выберете что Вас интересует:")

    await callback_query.message.answer_photo(
        photo=result["image"],
        caption=text,
        reply_markup=main_menu()
    )

    await callback_query.message.delete()

