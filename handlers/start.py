import sqlite3

from aiogram import types, Dispatcher
from config import bot
from const import START_TEXT
from database.sql_commands import Database
from keyboards.inlinebutton import start_keyboard


async def start(message: types.Message):
    Database().sql_insert_user_telegram(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    await bot.send_photo(chat_id=message.chat.id,
                         photo=open("/Users/ismarhahazov/MENTY/media/bot_pic.jpeg", 'rb'),
                         caption=START_TEXT.format(username=message.from_user.username),
                         parse_mode=types.ParseMode.MARKDOWN_V2,
                         reply_markup=await start_keyboard())


async def show_users(message: types.Message):
    users = Database().sql_select_user_command()

    if users:
        user_list_text = "Список пользователей:\n"
        for user in users:
            user_list_text += f"ID: {user[0]}, Username: {user[2]}\n"
    else:
        user_list_text = "В базе данных нет зарегистрированных пользователей."

    await message.answer(user_list_text)


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(show_users, commands=['showusers'])
