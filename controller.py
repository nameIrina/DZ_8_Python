from DZ_8_Python.data_import import data_import
from DZ_8_Python.data_export import data_export
from DZ_8_Python.data_print import data_print
import DZ_8_Python.data_search as fc
import DZ_8_Python.log as lg


def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_num = input("Введите телефон: ")
    return [last_name, first_name, phone_num]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def choice_todo():
    print("Что сделать:\n\
    1 - импорт;\n\
    2 - экспорт справочника;\n\
    3 - поиск контакта.")
    
    ch = input("Введите цифру: ")
    if ch == '1':
        lg.logging.info('Пользователь завел контакт')
        sep = choice_sep()
        data_import(input_data(), sep)
    
    elif ch == '2':
        lg.logging.info('Пользователь экспортировал справочник')
        data_print(data_export())
    
    elif ch == '3':
        lg.logging.info('Пользователь осуществлял поиск контакта')
        line = fc.find()
        print(line)