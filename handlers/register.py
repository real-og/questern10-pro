from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State


@dp.message_handler(state=State.entering_name)
async def send_welcome(message: types.Message, state: FSMContext):
    await state.update_data(team_name=message.text)
    await state.update_data(score_1='0')
    await state.update_data(score_2='0')
    await state.update_data(score_3='0')
    await message.answer(texts.success_register, reply_markup=kb.begin_quest_kb)
    await State.entering_begin_button.set()


@dp.message_handler(state=State.entering_begin_button)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.begin_quest_btn:
        await message.answer(texts.instruction, reply_markup=kb.levels_kb)
        await State.entering_level.set()
    else:
        await message.answer(texts.use_button, reply_markup=kb.begin_quest_kb)



