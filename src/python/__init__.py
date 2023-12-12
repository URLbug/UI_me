import json

from aiogram import Bot


config_bot = json.load(open('src/python/config_bot.json', 'rb'))
config_db = json.load(open('src/php/config.json', 'rb'))

bot = Bot(config_bot['TOKEN'])