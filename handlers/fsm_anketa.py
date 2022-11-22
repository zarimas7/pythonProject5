from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot
from keyboards.client_kb import submit_markup, cancel_markup, part_markup
from database.bot_db import sql_command_insert
from config import ADMINS


class FSMAdmin(StatesGroup):
    name = State()
    direct = State()
    age = State()
    grup = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id in ADMINS:
            await FSMAdmin.name.set()
            await message.answer('Привет, как звать?', reply_markup=cancel_markup)
    else:
        await message.answer('Пиши в личку!')


async def load_name (message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Какое направление?', reply_markup=submit_markup)


async def load_direct (message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['direct'] = message.text
    await FSMAdmin.next()
    await message.answer('Сколько вам лет?')



async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await FSMAdmin.next()
    await message.answer("Язык программирования?", reply_markup=part_markup)


async def load_grup(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['grup'] = message.text
        await message.answer(f"\nname: {data['name']}"
                             f"\ndirect: {data['direct']}"
                             f"\nage: {data['age']}"
                             f"\ngrup: {data['grup']}")
        await FSMAdmin.next()
        await message.answer("Данные правильные)?",  reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Все свободен!")
    elif message.text.lower() == "нет":
        await state.finish()
        await message.answer("Отмена")
    else:
        await message.answer("Нипонял!?")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Отмена")

def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direct, state=FSMAdmin.direct)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_grup, state=FSMAdmin.grup)
    dp.register_message_handler(submit, state=FSMAdmin.submit)