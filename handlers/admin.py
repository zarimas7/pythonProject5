from aiogram import Dispatcher, types
from config import bot, ADMINS
from database.bot_db import sql_command_all, sql_command_delete, sql_command_get_all_ids
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import choice


async def ban(message: types.Message):
    if message.chat.type == "group":
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой босс!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(message.chat.id,
                                       message.reply_to_message.from_user.id)
            await message.answer(f'{message.from_user.first_name} братан кикнул '
                                 f'{message.reply_to_message.from_user.full_name}')
    else:
        await message.answer("Пиши в группе!")


async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("Только админ может удалить данные!")
    else:
        mentors = await sql_command_all()
        for mentor in mentors:
            await message.answer(f"Number: {mentor[2]}"
                                 f"\nName: {mentor[1]}"
                                 f"\nGroup: {mentor[3]}"
                                 f"\nDepartment: {mentor[5]}"
                                 f"\nAge: {mentor[4]}"
                                 f"\nUsername: {mentor[6]}",
                                 reply_markup=InlineKeyboardMarkup().add(
                                     InlineKeyboardButton(f"delete {mentor[1]}",
                                                          callback_data=f"delete {mentor[0]}")))


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace('delete ', ''))
    await call.answer(text="удалено!", show_alert=True)
    await bot.delete_message(call.from_user.id, call.message.message_id)


async def rassylka(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("Ты не мой босс!")
    else:
        user_ids = await sql_command_get_all_ids()
        for user_id in user_ids:
            await bot.send_message(user_id[0], message.text.replace('/R ', ''))


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_message_handler(rassylka, commands=['R'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("delete "))