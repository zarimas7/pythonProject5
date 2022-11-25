import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer('Ok!')


async def go_to_drink_water():
    await bot.send_message(chat_id=chat_id, text="Иди выпей воды!")


async def to_smile():
    photo = open('media/cat_mBnN90j.jpg', 'rb')
    await bot.send_photo(chat_id=chat_id, photo=photo,
                         caption="Улыбнись!")




async def scheduler():
    aioschedule.every().day.at('08:00').do(go_to_drink_water)
    aioschedule.every().monday.at('07:00').do(to_smile)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'напомни' in word.text)