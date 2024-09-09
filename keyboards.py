from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import texts


begin_quest_kb = ReplyKeyboardMarkup([[texts.begin_quest_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

levels_kb = ReplyKeyboardMarkup([[texts.level1_btn, texts.level2_btn, texts.level3_btn,]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

cancel_level_kb = ReplyKeyboardMarkup([[texts.cancel_level_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

yes_no_kb = ReplyKeyboardMarkup([[texts.yes_btn, texts.no_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)
