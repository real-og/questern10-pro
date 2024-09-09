from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import checkers
import tables


@dp.message_handler(regexp=texts.level2_btn, state=State.entering_level)
async def send_welcome(message: types.Message, state: FSMContext):
    data = await state.get_data()
    levels = data.get('levels')
    if '2' in levels:
        await message.answer(texts.already_passed, reply_markup=kb.levels_kb)
        return
    await message.answer(texts.level2, reply_markup=kb.cancel_level_kb)
    levels.append('2')
    await state.update_data(levels=levels)
    await State.level2.set()


@dp.message_handler(state=State.level2)
async def send_welcome(message: types.Message, state: FSMContext):
    ans = message.text

    if ans == texts.cancel_level_btn:
        data = await state.get_data()
        score_2 = data.get('score_2') 
        await message.answer(texts.generate_score(score_2), reply_markup=kb.levels_kb)
        await State.entering_level.set()
        if len(data.get('levels')) == 3:
            await message.answer(texts.end)
        await tables.change_score(message.from_user.id, score_2, 2)
        return
    
    ans = ans.upper().replace('Ё', 'Е')
    if ans == 'Летом песня сама поется.'.upper():
        data = await state.get_data()
        if data.get('ans2_1') == '0':
            await message.answer(texts.level2_complete1)
            score_2 = data.get('score_2') 
            await state.update_data(score_2=int(score_2) + 1)
            await state.update_data(ans2_1='1')
        else:
            await message.answer(texts.already_done)

    elif ans == 'Убегающее лето — уходящий друг.'.upper() or ans == 'Убегающее лето — уходящий друг.'.upper():
        data = await state.get_data()
        if data.get('ans2_2') == '0':
            await message.answer(texts.level2_complete1)
            score_2 = data.get('score_2') 
            await state.update_data(score_2=int(score_2) + 1)
            await state.update_data(ans2_1='1')
        else:
            await message.answer(texts.already_done)
    elif ans == 'Лето — это улыбка, поцелуй и глоток вина.'.upper() or ans == 'Лето - это улыбка, поцелуй и глоток вина.'.upper():
        data = await state.get_data()
        if data.get('ans2_3') == '0':
            await message.answer(texts.level2_complete1)
            score_2 = data.get('score_2') 
            await state.update_data(score_2=int(score_2) + 1)
            await state.update_data(ans2_1='1')
        else:
            await message.answer(texts.already_done)

    elif ans == 'Лето просто открывает дверь и выпускает вас.'.upper():
        data = await state.get_data()
        if data.get('ans2_4') == '0':
            await message.answer(texts.level2_complete2)
            score_2 = data.get('score_2') 
            await state.update_data(score_2=int(score_2) + 2)
            await state.update_data(ans2_1='1')
        else:
            await message.answer(texts.already_done)
    elif ans == 'Одни из лучших воспоминаний связаны со шлепанцами.'.upper():
        data = await state.get_data()
        if data.get('ans2_5') == '0':
            await message.answer(texts.level2_complete2)
            score_2 = data.get('score_2') 
            await state.update_data(score_2=int(score_2) + 2)
            await state.update_data(ans2_1='1')
        else:
            await message.answer(texts.already_done)
    elif ans == 'Лето поет от радости, а пляжи манят танцующими волнами.'.upper():
        data = await state.get_data()
        if data.get('ans2_6') == '0':
            await message.answer(texts.level2_complete2)
            score_2 = data.get('score_2') 
            await state.update_data(score_2=int(score_2) + 2)
            await state.update_data(ans2_1='1')
        else:
            await message.answer(texts.already_done)
    elif ans == 'Летом, когда жарко, можно вытянуться и коснуться неба.'.upper():
        data = await state.get_data()
        if data.get('ans2_7') == '0':
            await message.answer(texts.level2_complete2)
            score_2 = data.get('score_2') 
            await state.update_data(score_2=int(score_2) + 2)
            await state.update_data(ans2_1='1')
        else:
            await message.answer(texts.already_done)

    elif ans == 'Лето — это ежегодное разрешение быть ленивым. Лежать в траве и считать звезды. Сидеть на бревне и изучать облака.'.upper() or ans == 'Лето - это ежегодное разрешение быть ленивым. Лежать в траве и считать звезды. Сидеть на бревне и изучать облака.'.upper():
        data = await state.get_data()
        if data.get('ans2_8') == '0':
            await message.answer(texts.level2_complete3)
            score_2 = data.get('score_2') 
            await state.update_data(score_2=int(score_2) + 3)
            await state.update_data(ans2_1='1')
        else:
            await message.answer(texts.already_done)
    elif ans == 'Лето — это возможность танцевать под солнцем и носить полевые цветы в волосах.'.upper() or ans == 'Лето - это возможность танцевать под солнцем и носить полевые цветы в волосах.'.upper():
        data = await state.get_data()
        if data.get('ans2_9') == '0':
            await message.answer(texts.level2_complete3)
            score_2 = data.get('score_2') 
            await state.update_data(score_2=int(score_2) + 3)
            await state.update_data(ans2_1='1')
        else:
            await message.answer(texts.already_done)
    elif ans == 'Нежность цветов, дыханье рассвета, таинство снов, высь облаков, легкость ветров — все это лето.'.upper() or ans == 'Нежность цветов, дыханье рассвета, таинство снов, высь облаков, легкость ветров - все это лето.'.upper():
        data = await state.get_data()
        if data.get('ans2_10') == '0':
            await message.answer(texts.level2_complete3)
            score_2 = data.get('score_2') 
            await state.update_data(score_2=int(score_2) + 3)
            await state.update_data(ans2_1='1')
        else:
            await message.answer(texts.already_done)
    else:
        await message.answer(texts.wrong_ans, reply_markup=kb.cancel_level_kb)
    
    