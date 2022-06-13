
import control


print('Вас приветствует телефонный справочник ')
power_on = True
func_select = control.function_select()
while power_on:
    if func_select == 1:
            get_data = control.get_card()
            if get_data == 1:
                while True:
                    search_select = control.search_select()
                    if search_select == 1:
                        print('В процессе ')
                        search_select = control.search_select()
                    if search_select == 2:
                        print('В процессе ')
                        search_select = control.search_select()
                    if search_select == 3:
                        break     
                    else: 
                        print('Вы ввели недопустимое значение, попробуйте снова!')
                        search_select = control.search_select()
            if get_data == 2:
                while True:
                    search_select = control.search_select()
                    if search_select == 1:
                        print('В процессе ')
                        search_select = control.search_select()
                    if search_select == 2:
                        print('В процессе ')
                        search_select = control.search_select()
                    if search_select == 3:
                        break       
            if get_data == 3:
                func_select = control.function_select()          
    if func_select == 2:
            while True:
                print('Предупреждение! Будьте внимательны при работе в данном разделе! ')
                redact = control.library_redact()
                if redact == 1:
                    card = control.new_card()
                    print(f'Новая карточка {card} добавлена в справочник ')
                if redact == 2:
                    func_select = control.function_select()
                    break
                else: 
                        print('Вы ввели недопустимое значение, попробуйте снова!')
                        redact = control.library_redact()
    if func_select == 3:
            print('Спасибо, что пользуетесь нашим приложением. До свидания ')
            print()
            power_on = False
 
