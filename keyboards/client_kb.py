from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
)

start_button = KeyboardButton("/start")
info_button = KeyboardButton("/info")
quiz_button = KeyboardButton("/quiz")

share_location = KeyboardButton("Share location", request_location=True)
share_contact = KeyboardButton("Share contact", request_contact=True)

start_markup.add(start_button, info_button, quiz_button,
                 share_location, share_contact)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("ДА"),
    KeyboardButton("НЕТ"),
)

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("CANCEL")
)

part_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=3
).add(
    KeyboardButton("JAVA"),
    KeyboardButton("PHP"),
    KeyboardButton("JAVASCRIPTS"),
    KeyboardButton('C++'),
    KeyboardButton('PYTHON')
)