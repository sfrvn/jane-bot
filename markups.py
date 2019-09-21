from telebot import types

source_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
source_markup_r1btn1 = types.KeyboardButton('Новые вакансии')
source_markup_r1btn2 = types.KeyboardButton('Все вакансии')
source_markup_r2btn1 = types.KeyboardButton('Без опыта')
source_markup_r2btn2 = types.KeyboardButton('Помощь')
source_markup.add(source_markup_r1btn1, source_markup_r1btn2, source_markup_r2btn1, source_markup_r2btn2)