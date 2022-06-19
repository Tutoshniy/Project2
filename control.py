import data_input
import csv

def function_select():
    func_select = input("""Выберите режим работы:
 1. Поиск абонента или номера телефона
 2. Редактор справочника
 3. Открыть справочник
 4. Выход """)    
    print()
    if not func_select.isdigit(): 
        print('Вы ввели недопустимое значение, попробуйте снова ')
        func_select = function_select()
    elif int(func_select)<1 or int(func_select)>4:
        print('Вы ввели недопустимое значение, попробуйте снова ')
        func_select = function_select()       
    else:
        print()
    return int(func_select)

def search_select():
    srch_select = input("""Выберите режим поиска:
        1. Поиск по имени
        2. Поиск по номеру телефона
        3. Назад """)
    print()
    if not srch_select.isdigit() and int(srch_select)<1 or int(srch_select)>3:
        print('Вы ввели недопустимое значение, попробуйте снова ')
        srch_select = search_select()
    print()
    return int(srch_select)


def get_card():
    get_data = input("""Найти номер телефона или карточку абонента?
        1. Номер телефона
        2. Карточку абонента
        3. Назад """)
    print()
    if not get_data.isdigit() and int(get_data)<1 or int(get_data)>3:
        print('Вы ввели недопустимое значение, попробуйте снова ')
        get_data = get_card()
    print()
    return int(get_data)


def new_card():
    card = data_input.card_creator()
    return card

def add_card(card):
    data_input.library_fill(card)


def library_redact():
    redact = input("""Выберите действие: 
        1. Создать новую карточку
        2. Удалить карточку
        3. Назад """)
    if not redact.isdigit() and int(redact)<1 or int(redact)>3:
        print('Вы ввели недопустимое значение, попробуйте снова ')
        redact = library_redact()
    print()
    return int(redact)

def card_check():
    get_data = input(''' 
    1. Добавить карточку
    2. Редактировать ''')
    print()
    if not get_data.isdigit() and int(get_data)<1 or int(get_data)>2:
        print('Вы ввели недопустимое значение, попробуйте снова ')
        get_data = get_card()
    print()
    return int(get_data)

def delete_card(line):
    new_lib =''
    with open('library.csv', 'r', encoding='utf_8') as lib:
            csv.register_dialect('my_dialect', delimiter='|', lineterminator="\r\n")
            reader = csv.reader(lib, 'my_dialect')
            for row in reader:
                if row!=line:
                    new_lib+=row+'\n'
            return new_lib


