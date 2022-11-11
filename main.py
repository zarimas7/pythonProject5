from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from decouple import config
# import logging


TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name}")
    # await message.answer("This is an answer method!")
    # await message.reply("This is an reply method!")

@dp.message_handler(commands=['quiz'])
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

    @dp.callback_query_handler(text="button_call_1")
    async def quiz_2(call: types.CallbackQuery):
        markup = InlineKeyboardMarkup()
        button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
        markup.add(button_call_2)

        question = "Сколько полос на флаге США?"
        answers = [
            "15",
            "12",
            "13",
            "20",
            "17",
            "19",
        ]

        await bot.send_poll(
            chat_id=call.from_user.id,
            question=question,
            options=answers,
            is_anonymous=False,
            type='quiz',
            correct_option_id=2,
            explanation="Иди учи python",
            open_period=10,
            reply_markup=markup
        )

        @dp.callback_query_handler(lambda call: call.data == "button_call_2")
        async def quiz_2(call: types.CallbackQuery):

            photo = open("media/cat_mBnN90j.jpg", 'rb')
            await bot.send_photo(call.from_user.id, photo=photo)



@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)



if __name__ == "__main__":

    executor.start_polling(dp, skip_updates=True)
