from aiogram import md, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards import keyboards as kb
from loader import dp
from states import states as st
from texts import numeric_keyboard as nk
from texts import text_buttons as tb
from texts import texts
from texts import questions
from utils import bd
from plotter_interpreter import *
from level_counter import *

# from handlers import start


@dp.message_handler(Text(equals=tb.start_menu[0], ignore_case=True), state='*')
async def analyst_start(message: types.Message):
    await st.StateQuestionnaire.question1.set()
    await message.answer(questions.team_problems,
                         reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))


@dp.message_handler(state=st.StateQuestionnaire.question1)
async def quest1(message: types.Message, state: FSMContext):
    tg_id = message.chat.id
    
    # TODO: обработать ситуацию /start
    # if message.text == '/start':
    #     await message.reply(texts.transfer_warning,
    #                         reply_markup=kb.add_step_keyboard(nk.numeric_keyboard))
    #     return

    if message.text.upper() not in nk.numeric_keyboard[:6]:
        await message.reply(texts.alert,
                            reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))
        return

    # Запишем ответ в базу
    bd.update_one_var(tg_id, 'question1', message.text)
    # Запишем ответ в состояние
    await state.update_data(quest1=message.text)
    # Вызовем следующее состояние
    await st.StateQuestionnaire.next()
    # Зададим следующий вопрос
    await message.answer(questions.solution,
                            reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))


@dp.message_handler(state=st.StateQuestionnaire.question2)
async def quest2(message: types.Message, state: FSMContext):
    tg_id = message.chat.id

    if message.text.upper() not in nk.numeric_keyboard[:6]:
        await message.reply(texts.alert,
                            reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))
        return

    bd.update_one_var(tg_id, 'question2', message.text)
    await state.update_data(quest2=message.text)
    await st.StateQuestionnaire.next()
    
    await message.answer(questions.planning_problems,
                         reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))



@dp.message_handler(state=st.StateQuestionnaire.question3)
async def quest3(message: types.Message, state: FSMContext):
    tg_id = message.chat.id
    
    if message.text.upper() not in nk.numeric_keyboard[:6]:
        await message.reply(texts.alert,
                            reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))
        return

    bd.update_one_var(tg_id, 'question3', message.text)
    await state.update_data(quest3=message.text)
    await st.StateQuestionnaire.next()

    await message.answer(questions.solution,
                         reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))


@dp.message_handler(state=st.StateQuestionnaire.question4)
async def quest4(message: types.Message, state: FSMContext):
    tg_id = message.chat.id

    if message.text.upper() not in nk.numeric_keyboard[:6]:
        await message.reply(texts.alert,
                            reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))
        return
    
    bd.update_one_var(tg_id, 'question4', message.text)
    await state.update_data(quest4=message.text)
    await st.StateQuestionnaire.next()
    await message.answer(questions.stakeholders_problems,
                         reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))


@dp.message_handler(state=st.StateQuestionnaire.question5)
async def quest5(message: types.Message, state: FSMContext):
    tg_id = message.chat.id
    
    if message.text.upper() not in nk.numeric_keyboard[:6]:
        await message.reply(texts.alert,
                            reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))
        return

    bd.update_one_var(tg_id, 'question5', message.text)

    
    await state.update_data(quest5=message.text)
    await st.StateQuestionnaire.next()
    await message.answer(questions.solution,
                         reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))



@dp.message_handler(state=st.StateQuestionnaire.question6)
async def quest6(message: types.Message, state: FSMContext):
    tg_id = message.chat.id
    
    if message.text.upper() not in nk.numeric_keyboard[:6]:
        await message.reply(texts.alert,
                            reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))
        return

    bd.update_one_var(tg_id, 'question6', message.text)

    await state.update_data(quest6=message.text)
    await st.StateQuestionnaire.next()
    await message.answer(questions.metrics_problems,
                         reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))



@dp.message_handler(state=st.StateQuestionnaire.question7)
async def quest7(message: types.Message, state: FSMContext):
    tg_id = message.chat.id

    if message.text.upper() not in nk.numeric_keyboard[:6]:
        await message.reply(texts.alert,
                            reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))
        return

    bd.update_one_var(tg_id, 'question7', message.text)
    await state.update_data(quest7=message.text)
    await st.StateQuestionnaire.next()
    await message.answer(questions.solution,
                         reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))


@dp.message_handler(state=st.StateQuestionnaire.question8)
async def quest8(message: types.Message, state: FSMContext):
    tg_id = message.chat.id

    if message.text.upper() not in nk.numeric_keyboard[:6]:
        await message.reply(texts.alert,
                            reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))
        return
    
    bd.update_one_var(tg_id, 'question8', message.text)

    await state.update_data(quest8=message.text)
    await st.StateQuestionnaire.next()
    await message.answer(questions.approach_problems,
                         reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))



@dp.message_handler(state=st.StateQuestionnaire.question9)
async def quest9(message: types.Message, state: FSMContext):
    tg_id = message.chat.id

    if message.text.upper() not in nk.numeric_keyboard[:6]:
        await message.reply(texts.alert,
                            reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))
        return

    bd.update_one_var(tg_id, 'question9', message.text)
    await state.update_data(quest9=message.text)
    await st.StateQuestionnaire.next()
    await message.answer(questions.solution,
                         reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))



@dp.message_handler(state=st.StateQuestionnaire.question10)
async def quest10(message: types.Message, state: FSMContext):
    tg_id = message.chat.id

    if message.text.upper() not in nk.numeric_keyboard[:6]:
        await message.reply(texts.alert,
                            reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))
        return

    bd.update_one_var(tg_id, 'question10', message.text)
    await state.update_data(quest10=message.text)
    await st.StateQuestionnaire.next()
    await message.answer(questions.risks_problems,
                         reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))


@dp.message_handler(state=st.StateQuestionnaire.question11)
async def quest11(message: types.Message, state: FSMContext):
    tg_id = message.chat.id

    if message.text.upper() not in nk.numeric_keyboard[:6]:
        await message.reply(texts.alert,
                            reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))
        return

    bd.update_one_var(tg_id, 'question11', message.text)
    await state.update_data(quest11=message.text)
    await st.StateQuestionnaire.next()
    await message.answer(questions.solution,
                         reply_markup=kb.add_step_keyboard(nk.numeric_keyboard[:6]))


@dp.message_handler(state=st.StateQuestionnaire.question12)
async def quest12(message: types.Message, state: FSMContext):
    tg_id = message.chat.id
    
    if message.text.upper() not in nk.numeric_keyboard:
        await message.reply(texts.range_alert,
                            reply_markup=kb.add_step_keyboard(nk.numeric_keyboard))
        return

    bd.update_one_var(tg_id, 'question12', message.text)
    await state.update_data(quest12=message.text)
    await st.StateQuestionnaire.next()
    await message.answer(questions.team_instruments,
                         reply_markup=types.ReplyKeyboardRemove())
    

@dp.message_handler(state=st.StateQuestionnaire.question13)
async def quest13(message: types.Message, state: FSMContext):
    tg_id = message.chat.id
    
    if message.text.upper() not in nk.numeric_keyboard:
        await message.reply(texts.range_alert,
                            reply_markup=types.ReplyKeyboardRemove())
        return

    bd.update_one_var(tg_id, 'question13', message.text)
    await state.update_data(quest13=message.text)
    await st.StateQuestionnaire.next()
    await message.answer(questions.planning_instruments,
                         reply_markup=types.ReplyKeyboardRemove())
    

@dp.message_handler(state=st.StateQuestionnaire.question14)
async def quest14(message: types.Message, state: FSMContext):
    tg_id = message.chat.id
    if message.text.upper() not in nk.numeric_keyboard:
        await message.reply(texts.range_alert,
                            reply_markup=types.ReplyKeyboardRemove())
        return

    bd.update_one_var(tg_id, 'question14', message.text)
    await state.update_data(quest14=message.text)
    await st.StateQuestionnaire.next()
    await message.answer(questions.stakeholders_instruments,
                         reply_markup=types.ReplyKeyboardRemove())
    

@dp.message_handler(state=st.StateQuestionnaire.question15)
async def quest15(message: types.Message, state: FSMContext):
    tg_id = message.chat.id

    if message.text.upper() not in nk.numeric_keyboard:
        await message.reply(texts.range_alert,
                            reply_markup=types.ReplyKeyboardRemove())
        return

    bd.update_one_var(tg_id, 'question15', message.text)
    await state.update_data(quest15=message.text)
    await st.StateQuestionnaire.next()
    await message.answer(questions.metrics_instruments,
                         reply_markup=types.ReplyKeyboardRemove())
    

@dp.message_handler(state=st.StateQuestionnaire.question16)
async def quest16(message: types.Message, state: FSMContext):
    tg_id = message.chat.id
    
    if message.text.upper() not in nk.numeric_keyboard:
        await message.reply(texts.range_alert,
                            reply_markup=types.ReplyKeyboardRemove())
        return

    bd.update_one_var(tg_id, 'question16', message.text)
    await state.update_data(quest16=message.text)
    await st.StateQuestionnaire.next()
    await message.answer(questions.approach_instruments,
                         reply_markup=types.ReplyKeyboardRemove())
    

@dp.message_handler(state=st.StateQuestionnaire.question17)
async def quest17(message: types.Message, state: FSMContext):
    tg_id = message.chat.id

    if message.text.upper() not in nk.numeric_keyboard:
        await message.reply(texts.range_alert,
                            reply_markup=types.ReplyKeyboardRemove())
        return

    bd.update_one_var(tg_id, 'question17', message.text)
    await state.update_data(quest17=message.text)
    await st.StateQuestionnaire.next()
    await message.answer(questions.risks_instruments,
                         reply_markup=types.ReplyKeyboardRemove())
    

@dp.message_handler(state=st.StateQuestionnaire.question18)
async def quest18(message: types.Message, state: FSMContext):
    tg_id = message.chat.id
    
    if message.text.upper() not in nk.numeric_keyboard:
        await message.reply(texts.range_alert,
                            reply_markup=types.ReplyKeyboardRemove())

    bd.update_one_var(tg_id, 'question18', message.text)
    await state.update_data(quest18=message.text)
    await state.finish()  # Закроем машину состояний
    bd.finish(tg_id, 'True')

    await message.answer(questions.finish,
                            reply_markup=types.ReplyKeyboardRemove())

    # Выберем запись из БД
    result_lst = bd.result(tg_id)
    create_chart(result_lst)
    
    # Отправим паутинку в чат
    with open(f"{os.environ['SYSTEM_PATH']}{result_lst[0]}.jpeg", "rb") as img:
        await message.answer_photo(img)

    await message.answer(level_count(result_lst), disable_web_page_preview=True)
    await message.answer(interprete_score(result_lst))
    append_result(result_lst)