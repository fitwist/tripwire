import re
from aiogram import md, types
from aiogram.utils.deep_linking import get_start_link, decode_payload
from aiogram.dispatcher import filters
from keyboards import keyboards as kb
from texts import texts, text_buttons as texts_btn
from utils import bd
from loader import *


@dp.message_handler(commands=['start'], state=None)
async def start(message: types.Message):
    tg_id = message.chat.id

    if not bd.check_user(tg_id):
        await ask_phone(tg_id, message.chat.first_name)
    else:
        await message.answer(texts.initialize_questionnaire,reply_markup=kb.add_step_keyboard(texts_btn.start_menu))


async def ask_phone(tg_id, first_name):
    phone = kb.send_phone()
    name = md.bold(first_name)
    await bot.send_message(tg_id,
                           f'''Привет, {name}\!
Для регистрации нажми кнопку Передать номер телефона''',
                           reply_markup=phone)


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def get_phone(message: types.Message):
    phone = message.contact.phone_number
    name = message.contact.first_name
    tg_id = message.chat.id
    # user_data = bd.registration(tg_id, phone, name)
    bd.registration(tg_id, phone, name)

    await message.answer(md.text(
        texts.initialize_questionnaire,
        sep='\n'),
        reply_markup=kb.add_step_keyboard(texts_btn.start_menu))
