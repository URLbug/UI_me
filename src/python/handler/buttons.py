from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def menu() -> ReplyKeyboardMarkup:
    build = ReplyKeyboardBuilder()

    build.button(text='Войти')
    build.button(text='Регестрация')

    build.adjust(2)

    return build.as_markup(resize_keyboard=True)

def registrs() -> ReplyKeyboardMarkup:
    build = ReplyKeyboardBuilder()

    build.button(text='Меню')

    build.adjust(2)

    return build.as_markup(resize_keyboard=True)