from aiogram import  Dispatcher, types
from config import bot, dp
import random


# @dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric():
        await bot.send_message(message.chat.id, int(message.text) ** 2)
    else:
        await bot.send_message(message.chat.id, message.text)

    if message.text.startswith('!pin'):
        if message.reply_to_message:
            await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.text == 'game':
        await bot.send_dice(message.chat.id, emoji=random.choice(['🎰', '🎳', '🎯', '🎲', '🏀', '⚽']))


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)