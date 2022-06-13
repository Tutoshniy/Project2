
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
                        get_data = control.get_card()
                    else: 
                        print('Вы ввели недопустимое значение, попробуйте снова!')
                        search_select = control.search_select()
            if get_data == 2:
                while True:
                    search_select = control.search_select()
            if get_data == 3:
                func_select = control.function_select()          
    if func_select == 2:
            print('В процессе')
            func_select = control.function_select()
    if func_select == 3:
            print('Спасибо, что пользуетесь нашим приложением. До свидания ')
            print()
            power_on = False
    else:
        print('Вы ввели недопустимое значение, попробуйте снова ')
        func_select = control.function_select()

