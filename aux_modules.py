import json, requests, os
from dotenv import load_dotenv

URL = 'https://api.hh.ru/vacancies'

PAYLOAD = {
    'text': 'стажировка дизайн',
    'per_page': '100', 
    'area': 1, # Moscow,
    'specialization': ['20.36', '11.62', '3.64']
}

EXCEPTIONS = ['интерьер', 'ландшафт', 'мебели']

def count_vacancies(vacs_dict):
    counter = 0
    for vacancy in vacs_dict:
        counter += 1
    return counter

def perdict_salary(salary):
    if salary:
        if not salary['from']:
            return salary['to']
        elif not salary['to']:
            return salary['from']
        else:
            return 'от {} до {}'.format(salary['from'], salary['to'])
    else:
        return 'не знаю, сколько... У них не написано'

def perdict_address(address):
    if address and address['metro']:
        return address['metro']['station_name']
    else:
        return 'не знаю, какое. Может, найдётся по ссылке...'

def make_vacs_dict():
    vacancy_dict = {}

    response = requests.get(URL, PAYLOAD).json()

    for vacancy in response['items']:
        publish = True
        for exept in EXCEPTIONS:
            if exept in vacancy['name']:
                publish = False
        if publish:
            vacancy_dict[vacancy['id']] = {
                'name': vacancy['name'],
                'salary': perdict_salary(vacancy['salary']),
                'address': perdict_address(vacancy['address']),
                'employer': vacancy['employer']['name'],
                'vacancy_url': vacancy['alternate_url'],
                'description': vacancy['snippet']['requirement'],
                'vacancy_date': vacancy['published_at']
            }
    
    return vacancy_dict

def update_new_vacs():
    id_list = []
    with open('old_vacs.json', 'r') as old_vacs:
        old_vacs_dict = json.load(old_vacs)
        for vacancy in old_vacs_dict:
            id_list.append(vacancy)
    with open('new_vacs.json', 'r') as new_vacs:
        new_vacs_dict = json.load(new_vacs)
        for vacancy in new_vacs_dict:
            id_list.append(vacancy)
        response_vacs = make_vacs_dict()
        for vacancy in response_vacs:
            if not vacancy in id_list:
                new_vacs_dict[vacancy] = response_vacs[vacancy]

    with open('new_vacs.json', 'w') as new_vacs:
        new_vacs.write(json.dumps(new_vacs_dict))
    
def get_no_work_experience_vacs():
    payload_nwe = PAYLOAD
    payload_nwe['experience'] = 'noExperience'
    response_url = requests.get(URL, payload_nwe).json()['alternate_url']
    return response_url
