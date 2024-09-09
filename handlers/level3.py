from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import checkers
import tables


@dp.message_handler(regexp=texts.level3_btn, state=State.entering_level)
async def send_welcome(message: types.Message, state: FSMContext):
    data = await state.get_data()
    levels = data.get('levels')
    if '3' in levels:
        await message.answer(texts.already_passed, reply_markup=kb.levels_kb)
        return
    await message.answer(texts.level3, reply_markup=kb.cancel_level_kb)
    levels.append('3')
    await state.update_data(levels=levels)
    await State.level3.set()



@dp.message_handler(state=State.level3)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = message.text

    if ans == texts.cancel_level_btn:
        data = await state.get_data()
        score_3 = data.get('score_3') 
        await message.answer(texts.generate_score(score_3), reply_markup=kb.levels_kb)
        await State.entering_level.set()
        if len(data.get('levels')) == 3:
            await message.answer(texts.end)
        await tables.change_score(message.from_user.id, score_3, 3)
        return

    if ans.lower() in checkers.level3_anses:
        index = checkers.level3_anses.index(ans.lower())
        data = await state.get_data()
        indexes = data.get('indexes')
        if index in indexes:
            await message.answer(texts.already_done)
        else:
            await message.answer(texts.level2_complete1)
            score_3 = data.get('score_3')
            await state.update_data(score_3=int(score_3) + 1)
            indexes.append(index)
            await state.update_data(indexes=indexes)
    else:
        await message.answer(texts.wrong_ans, reply_markup=kb.cancel_level_kb)


