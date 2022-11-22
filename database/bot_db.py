import random
import sqlite3
from config import bot

def sql_create():
    global db, cursor
    db = sqlite3.connect("mentors.sqlite3")
    cursor = db.cursor()

    if db:
        print('База данных подключена!')

    db.execute('CREATE TABLE IF NOT EXISTS anketa'
               '(name TEXT,'
               'direct TEXT, age INTEGER, grup INTEGER)')
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO anketa VALUES "
                       "(?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM anketa").fetchall()
    random_user = random.choice(result)
    await message.answer(f'Number: {random_user[2]}'
                         f'\nName: {random_user[1]}'
                         f'\nGroup:{random_user[5]}'
                         f'\ndirect:{random_user[3]}'
                         f'\n Age: {random_user[4]}')




async def sql_command_all():
    return cursor.execute("SELECT * FROM anketa").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM anketa WHERE id = ?", (user_id,))
    db.commit()


async def sql_command_get_all_ids():
    return cursor.execute("SELECT id FROM anketa").fetchall()

