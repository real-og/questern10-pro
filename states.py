from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    entering_name = State()
    entering_begin_button = State()
    entering_level = State()
    level1 = State()
