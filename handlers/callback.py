from aiogram import  Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp



# @dp.callback_query_handler(text="button_call_1")
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

# @dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quiz_3(call: types.CallbackQuery):

            photo = open("media/cat_mBnN90j.jpg", 'rb')
            await bot.send_photo(call.from_user.id, photo=photo)


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text = "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")
