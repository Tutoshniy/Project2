import csv
from encodings import utf_8

def library_read(): 
        with open('library.csv', 'r', encoding='utf_8') as lib:
            csv.register_dialect('my_dialect', delimiter='|', lineterminator="\r\n")
            reader = csv.reader(lib, 'my_dialect')
            for row in reader:
                print(row)