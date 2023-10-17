from aiogram import types, Dispatcher
from config import bot
from const import START_TEXT
from database.sql_commands import Database
from keyboards.inlinebutton import first_question


async def start_questionnarie_call(call: types.CallbackQuery):
    await bot.send_message(chat_id=call.from_user.id,
                           text='Выбери правильный выбор:',
                           reply_markup=await first_question()
                           )


async def rightquestion(call: types.CallbackQuery):
    Database().sql_update_user_count_command(telegram_id=call.from_user.id)
    await bot.send_message(chat_id=call.from_user.id,
                           text='Правильно')


async def wrongquestion(call: types.CallbackQuery):
    Database().sql_update_user_count_minus_command(telegram_id=call.from_user.id)
    await bot.send_message(chat_id=call.from_user.id,
                           text='Не правильно')


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnarie_call, lambda call: call.data == 'start Questionnaire')
    dp.register_callback_query_handler(rightquestion, lambda call: call.data == 'right')
    dp.register_callback_query_handler(wrongquestion, lambda call: call.data == 'wrong')
