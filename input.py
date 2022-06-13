import csv
from encodings import utf_8

def name_input():
    symbols = "!'@#$%^&*()`/:;.,?<>\|'""+ -=[]}{"
    obj = input('Введите ФИО абонента в формате Иванов Иван Иванович: ')
    while True:
        for char in obj:
            if char.isdigit() or char.isalnum() or char in symbols:
                return obj
            else:
                print('Вы ввели недопустимый символ, попробуйте снова')    

def number_input():
    obj = input('Введите номер абонента в формате 8800123: ')
    while True: 
        for char in obj:
            if char.isdigit():
                return obj
            else:
                print('Вы ввели недопустимый символ, попробуйте снова ')    

def library_fill(card): #card - карточка абонента
    with open('library.csv', 'a', encoding='utf_8') as lib:
        csv.register_dialect('my_dialect', delimiter='|', lineterminator="\r\n")
        writer = csv.writer(lib, 'my_dialect')
        writer.writerow(card)
card = ['Иванов','Иван','Иванович','8800123','личный']   
library_fill(card)