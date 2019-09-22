import telebot, os
from telebot import types
from dotenv import load_dotenv
from aux_modules import *
from markups import source_markup

HELP = '''
Нажми на одну из кнопок или напиши /start, если кнопочки исчезли.\n
'''

bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Вижу, ты хочешь найти работу. Давай посмотрим, что для тебя найдется...\n' + HELP, reply_markup=source_markup)

def new_vacancies_handler(message):
    update_new_vacs()
    with open('new_vacs.json', 'r') as new_vacs:
        new_vacs_dict = json.load(new_vacs)
        old_vacs_list = []
        if new_vacs_dict:
            counter = count_vacancies(new_vacs_dict)
            if count_vacancies(new_vacs_dict) > 3:
                counter = 3
            for vacancy in new_vacs_dict:
                if counter == 0:
                    break
                old_vacs_list.append(vacancy)
                
                vacancy = new_vacs_dict[vacancy]

                link_markup = types.InlineKeyboardMarkup()
                link_markup_btn = types.InlineKeyboardButton('Линк на вакансию', url=vacancy['vacancy_url'])
                link_markup.add(link_markup_btn)

                answer = '*Вакансия:* {}\nПлатят *{}*\n*Метро:* {}\n'.format(
                    vacancy['name'], vacancy['salary'], vacancy['address'] 
                )
                if counter == 3:
                    bot.send_message(message.chat.id, 'Вот, что я для тебя нашла\n\n'+answer, parse_mode='Markdown', reply_markup=link_markup)
                else:
                    bot.send_message(message.chat.id, answer, parse_mode='Markdown', reply_markup=link_markup)
                counter -= 1
            if count_vacancies(new_vacs_dict)-3 > 0:
                bot.send_message(message.chat.id, 'Осталось {} новых вакансий.\nЕсли попросишь, могу скинуть ещё парочку'.format(count_vacancies(new_vacs_dict)-3))
        else:
            bot.send_message(message.chat.id, 'Ой, кажется, новых вакансий не осталось')

    with open('old_vacs.json', 'r') as old_vacs:
        old_vacs_dict = json.load(old_vacs)

    with open('old_vacs.json', 'w') as old_vacs:
        for vacancy_id in old_vacs_list:
            old_vacs_dict[vacancy_id] = new_vacs_dict[vacancy_id]
            del new_vacs_dict[vacancy_id]
        old_vacs.write(json.dumps(old_vacs_dict))
    with open('new_vacs.json', 'w') as new_vacs:
        new_vacs.write(json.dumps(new_vacs_dict))

def all_vacancies_handler(message):
    link_markup = types.InlineKeyboardMarkup()
    link_markup_btn = types.InlineKeyboardButton('Все вакансии', url=requests.get(URL, PAYLOAD).json()['alternate_url'])
    link_markup.add(link_markup_btn)
    bot.send_message(message.chat.id, 'Чтобы посмотреть все вакансии, которые мне удалось найти, нажми на кнопочку ниже', reply_markup=link_markup)

def no_work_experience_handler(message):
    link_markup = types.InlineKeyboardMarkup()
    link_markup_btn = types.InlineKeyboardButton('Вакансии без опыта', url=get_no_work_experience_vacs())
    link_markup.add(link_markup_btn)
    bot.send_message(message.chat.id, 'Чтобы посмотреть вакансии без опыта работы, нажми на кнопочку ниже', reply_markup=link_markup)

def help_handler(message):
    bot.send_message(message.chat.id, 'Видимо, что-то пошло не так, раз тебе понадобилась помощь. Ну ничего, попробуем разобраться \n' + HELP + 'Если я сломалась; если хочешь, чтобы я ещё чему-то научилась, напиши @sfrvn. Он должен помочь.')

@bot.message_handler(commands=['re'])
def refresh_handler(message):
    with open('old_vacs.json', 'w') as old_vacs:
        old_vacs.write(json.dumps({}))
    bot.send_message(message.chat.id, 'Я всё сделала. Проблем больше нет')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "новые вакансии":
        new_vacancies_handler(message)
    elif text == "все вакансии":
        all_vacancies_handler(message)
    elif text == "без опыта":
        no_work_experience_handler(message)
    elif text == "помощь":
        help_handler(message)
    else:
        bot.send_message(chat_id, 'Ой, я тебя не понимаю...\nНапиши *помощь*, и мы с тобой что-нибудь придумаем', parse_mode='Markdown')

bot.polling()