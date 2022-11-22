from aiogram import  Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
from keyboards.client_kb import start_markup
from database.bot_db import sql_command_random


# @dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name}")
    await message.answer("This is an answer method!")
    await message.reply("This is an reply method!")


async def info_handler(message: types.Message):
    await message.reply("Сам разбирайся!")


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Какой национальный цветок Японии?"
    answers = [
        "Роза",
        'Сакура',
        'Лилия',
        'Лотос',
        'Жасмин',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Иди учи историю",
        open_period=10,
        reply_markup=markup
    )

async def get_random_user(message:types.Message):
    await sql_command_random(message)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(get_random_user, commands=['get'])