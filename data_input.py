import csv
from encodings import utf_8
import collections

def name_input():
    symbols = "!'@#$%^&*()`/:;.,?<>\|'""+-=[]}{"
    name_format = collections.namedtuple('record_format', 'lastname first_name patername')
    name = name_format(lastname = input('Введите фамилию ').capitalize(), first_name = input('Введите имя ').capitalize(), patername = input('Введите отчество ').capitalize())
    while True:
        for char in name:
            if char.isdigit() or char in symbols:
                print('Вы ввели недопустимый символ, попробуйте снова')    
            else:
                return name

def number_input():
    obj = input('Введите номер телефона абонента: ')
    while True: 
        for char in obj:
            if char.isdigit():
                return obj
            else:
                print('Вы ввели недопустимый символ, попробуйте снова ')    

def library_fill(card):
        with open('library.csv', 'a', encoding='utf_8') as lib:
            csv.register_dialect('my_dialect', delimiter='|', lineterminator="\n")
            writer = csv.writer(lib, 'my_dialect')
            writer.writerow(card)

def card_creator():
    card = []
    name_format = collections.namedtuple('record_format', 'lastname first_name patername')
    name = name_format(lastname = input('Введите фамилию ').capitalize(), first_name = input('Введите имя ').capitalize(), patername = input('Введите отчество ').capitalize())
    phone_format = collections.namedtuple('record_format', 'phone phone_type')
    phone = phone_format(phone = input('Введите номер телефона: '), phone_type = input('Введите тип номера: '))
    card.append(name.lastname)
    card.append(name.first_name)
    card.append(name.patername)
    card.append(phone.phone)
    card.append(phone.phone_type)
    return card

# def library_del():
#     new_lib = ''
#     with open('library.csv', 'a', encoding='utf_8') as lib:
#             csv.register_dialect('my_dialect', delimiter='|', lineterminator="\r\n")
#             reader = csv.reader(lib, 'my_dialect')
#             for row in reader:
#                 if row != line:
#                     new_lib += row
#     print(new_lib)


