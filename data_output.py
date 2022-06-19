import csv
from encodings import utf_8
from prettytable import PrettyTable
import prettytable

def library_read(): 
        catalog = PrettyTable()
        catalog.field_names = ['Фамилия','Имя','Отчество','Номер телефона','Тип номера']
        with open('library.csv', 'r', encoding='utf_8') as lib:
            csv.register_dialect('my_dialect', delimiter='|', lineterminator="\r\n")
            reader = csv.reader(lib, 'my_dialect')
            for row in reader:
                if row != []:
                    catalog.add_row(row)
            print(catalog)
                