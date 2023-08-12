from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp
from texts import text_buttons as tb

meme_dir = 'data/memes/'


@dp.message_handler(Text(equals=tb.start_menu[1], ignore_case=True), state='*')
async def stop_questionaire(message: types.Message):
    await message.answer("Очень жаль\. Надеюсь, вы передумаете\. Вы всегда можете начать заново с помощью команды /start\.",
                         reply_markup=types.ReplyKeyboardRemove())