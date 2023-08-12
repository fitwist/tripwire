import random

from aiogram import md, types
from keyboards import keyboards as kb
from texts import text_buttons as tb
from texts import texts
from utils import bd


# async def fault(message: types.Message):
#     # Пометим игрока проигравшим
#     tg_id = message.chat.id
#     await message.answer(texts.fault,
#                          reply_markup=kb.add_step_keyboard(tb.start_menu))
#     bd.finish(tg_id, 'False', 'analyst')
#     bd.update_one_var(tg_id, 'count', 2)
#
#
# async def answer_not_correct(message: types.Message, count, state):
#     # При некорректном ответе вычтем из счетчика 1
#     tg_id = message.chat.id
#     count = int(count) - 1  # Вычтем единицу из попыток
#     bd.update_one_var(tg_id, 'count', count)  # запишем count в БД
#     if count == 0:
#         # Сбросим состояние и счетчик ("Вы проиграли")
#         await fault(message)
#         await state.finish()
#         return
#     text = f'Осталось попыток: {count}'
#     if count == 1:
#         text = f'Осталось попыток: {count}'
#     n = int(random.randint(0, 6))
#
#     await message.reply(md.text(
#         texts.answer_not_correct[n],
#         text,
#         sep='\n'
#     ))
