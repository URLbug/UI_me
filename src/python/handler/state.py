from aiogram.fsm.state import State, StatesGroup


class Login(StatesGroup):
    email = State()
    password = State()