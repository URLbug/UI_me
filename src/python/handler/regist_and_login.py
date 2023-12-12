import hashlib

from aiogram import Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters.text import Text
from aiogram.fsm.context import FSMContext

from database.conn import session
from database.class_db import User
from .buttons import registrs, menu
from .state import Login


route = Router()

@route.message(Text(text="Регестрация"))
async def regist(message: Message) -> Message:
    await message.answer(
        """
        Для того чтобы зарегестрироватся перейдите по этой ссылке
        http://localhost:8080/
        (Да, я знаю, что это веб сервер моего пк, но мне лень выладывать на хост)
        """,
        reply_markup=registrs()
    )

@route.message(Text(text='Войти'))
async def login_email(message: Message, state: FSMContext) -> Message:
    await message.answer('Напишите ваш email', reply_markup=ReplyKeyboardRemove())

    await state.set_state(Login.email)

@route.message(Login.email)
async def login_password(message: Message, state: FSMContext) -> Message:
    await state.update_data(email=message.text)

    await message.answer('Напишит ваш пароль')

    await state.set_state(Login.password)

@route.message(Login.password)
async def logins(message: Message, state: FSMContext) -> Message:
    login = await state.get_data()

    email = login['email']
    
    password = hashlib.md5(message.text.encode())
    password = password.hexdigest()

    usr = session.query(User).filter_by(email=email, password=password).first()

    if usr:
        await message.answer(f'Вы успешно вошли в свой аккаунт {usr.first_name} {usr.last_name}', reply_markup=menu())
    else:
        await message.answer('''
        Не верный пароль, либо email.
        Если вы не зарегестрированы то вы можете это сделать здесь -> http://localhost:8080/
        (Да, я знаю, что это веб сервер моего пк, но мне лень выладывать на хост)
        ''', reply_markup=menu())
    
    await state.clear()

