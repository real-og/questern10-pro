from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from states import State
import texts
import tables

@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.start_command1)
    await message.answer(texts.start_command2)
    await State.entering_name.set()
    await tables.append_user(message.from_user.id, message.from_user.username)


@dp.message_handler(commands=['help'], state="*")
async def send_help(message: types.Message, state: FSMContext):
    await message.answer(texts.help_command)