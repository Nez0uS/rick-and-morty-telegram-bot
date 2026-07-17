from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from services.rick_and_morty_api import RickAndMortyAPI
from keyboards.main_menu import main_menu

rick_and_morty_client = RickAndMortyAPI()
search_by_name_router = Router()

class SearchByName(StatesGroup):
    waiting_for_search = State()
    bot_message_id = State()


@search_by_name_router.callback_query(F.data == "search_by_name")
async def search_by_name(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await state.set_state(SearchByName.waiting_for_search)

    message = await callback_query.message.edit_text("Введите имя персонажа (пример: Rick, Morty):")
    await state.update_data(bot_message_id=message.message_id)

@search_by_name_router.message(SearchByName.waiting_for_search)
async def search_result(message: Message, state: FSMContext):
    data = await state.get_data()
    bot_message_id = data.get('bot_message_id')
    result = await rick_and_morty_client.search_by_name(message.text)

    text = (f"Вы ввели: {message.text}\n"
            f"Результат поиска:\n\n")

    for index, character in enumerate(result):
        text += f"{index + 1}. {character['name']}\n"

    text += f"\nНажмите, что хотите узнать:"

    await message.answer(text, reply_markup=main_menu())

    await message.delete()

    if bot_message_id:
        await message.bot.delete_message(
            chat_id=message.chat.id,
            message_id=bot_message_id
        )

    await state.clear()