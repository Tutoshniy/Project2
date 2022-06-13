import control
import interface
from interface import get_data
from control import search_select
import csv
from encodings import utf_8

def library_find(card): #card - карточка абонента
    with open('library.csv', encoding='utf_8') as lib:
        read_data = csv.reader(lib, delimiter="|")
        count = 0
        for data in read_data:
            if get_data == 1:
                search_data = read_data.find(search_select)
            elif get_data == 2:
                search_data = read_data.find(search_select)
            elif get_data == 3:
                break
        print(search_data)
