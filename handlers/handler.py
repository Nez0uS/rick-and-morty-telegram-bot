from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from keyboards.main_menu import main_menu


start_router = Router()


@start_router.message(CommandStart())
async def start_handler(msg: Message):
    await msg.answer(f"Привет, {msg.from_user.first_name}! Это бот по сериалу Rick и Morty!\nВыбери что тебя интересует:",
        reply_markup=main_menu()
    )


@start_router.callback_query(F.data == "main_menu")
async def show_main_menu(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.answer("Выбери: что тебя интересует",
        reply_markup=main_menu()
    )