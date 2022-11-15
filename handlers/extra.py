from aiogram import  Dispatcher, types
from config import bot, dp
from random import randint, choice

# @dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await bot.send_message(message.chat.id, int(message.text) ** 2)
    else:
        await bot.send_message(message.chat.id, message.text)

    if message.text.startswith('!pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.text == 'game':
        await bot.send_dice(message.chat.id, emoji='🎯')


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)