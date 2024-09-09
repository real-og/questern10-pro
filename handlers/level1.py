from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import checkers


@dp.message_handler(regexp=texts.level1_btn, state=State.entering_level)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.level1, reply_markup=kb.cancel_level_kb)
    await State.level1.set()


@dp.message_handler(state=State.level1)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = message.text

    if ans == texts.cancel_level_btn:
        data = await state.get_data()
        score_1 =  data.get('score_1') 
        await message.answer(texts.generate_score_1(score_1), reply_markup=kb.levels_kb)
        await State.entering_level.set()
        return

    if checkers.check_level_1(ans):
        await message.answer(texts.level1_complete1)
        await message.answer(texts.level1_complete2, reply_markup=kb.cancel_level_kb)
        await state.update_data(score_1='10')
    else:
        is_partly = False
        print()
        for correct_ans in checkers.level1_anses:
            print(ans.upper())
            print(correct_ans.upper())
            print(correct_ans.upper().find(ans.upper()))
            if correct_ans.upper().find(ans.upper()) > -1:
                is_partly = True
        if is_partly:
            await message.answer(texts.partly_ans, reply_markup=kb.cancel_level_kb)
        else:
            await message.answer(texts.wrong_ans, reply_markup=kb.cancel_level_kb)
    await State.level1.set()