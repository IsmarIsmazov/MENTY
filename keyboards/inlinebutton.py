from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Начать проверку",
        callback_data="start Questionnaire"
    )
    markup.add(
        questionnaire_button
    )
    return markup


async def first_question():
    markup = InlineKeyboardMarkup()
    first_button = InlineKeyboardButton(
        'Правильный ответ',
        callback_data='right'
    )
    second_button = InlineKeyboardButton(
        'Не правильный овтет',
        callback_data='wrong'
    )
    markup.add(first_button)
    markup.add(second_button)
    return markup
