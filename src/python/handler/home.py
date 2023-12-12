from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.filters.text import Text

from .buttons import menu


route = Router()

@route.message(Command('start'))
async def start(message: Message) -> Message:
    await message.answer("""
    Добро пожаловать в бота UI the me.
    Это мой небольшой pet проект для соеденения нескольких языков программирования.
    GitHub: https://github.com/URLbug
    """, reply_markup=menu())

@route.message(Text(text='Меню'))
async def main_menu(message: Message) -> Message:
    await message.answer("""
    Добро пожаловать в бота UI the me.
    Это мой небольшой pet проект для соеденения нескольких языков программирования.
    GitHub: https://github.com/URLbug
    """, reply_markup=menu())