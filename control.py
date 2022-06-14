import data_input

def function_select():
    func_select = input('Выберите режим работы:\
 1. Поиск абонента или номера телефона\
 2. Редактор справочника\
 3. Открыть справочник\
 4. Выход ')    
    if not func_select.isdigit() and int(func_select)<1 or int(func_select)>4: 
        print('Вы ввели недопустимое значение, попробуйте снова ')
        func_select = function_select()       
    else:
        print()
    return int(func_select)

def search_select():
    srch_select = input('Выберите режим поиска:\
        1. Поиск по имени\
        2. Поиск по номеру телефона\
        3. Назад ')
    if not srch_select.isdigit() and int(srch_select)<1 or int(srch_select)>3:
        print('Вы ввели недопустимое значение, попробуйте снова ')
        srch_select = search_select()
    print()
    return int(srch_select)


def get_card():
    get_data = input('Найти номер телефона или карточку абонента?\
        1. Номер телефона\
        2. Карточку абонента\
        3. Назад ')
    if not get_data.isdigit() and int(get_data)<1 or int(get_data)>3:
        print('Вы ввели недопустимое значение, попробуйте снова ')
        get_data = get_card()
    print()
    return int(get_data)


def new_card():
    card = data_input.card_creator()
    data_input.library_fill(card)
    return card


def library_redact():
    redact = input('Выберите действие: \
        1. Создать новую карточку\
        2. Назад ')
    if not redact.isdigit() and int(redact)<1 or int(redact)>2:
        print('Вы ввели недопустимое значение, попробуйте снова ')
        redact = library_redact()
    print()
    return int(redact)