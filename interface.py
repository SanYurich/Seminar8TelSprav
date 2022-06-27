import log_files as l_f
import add_files as a_f
# import edit_files as e_f
# import del_files as d_f
import output_files as o_f
import export as ex
import importer as im
import time

def add_oper():
    name = input(f"Название контакта: ")
    number = int(input(f"Номер телефона: "))
    
    a_f.add_contact(name, number,"spravochnik.txt")

# def edit_oper():
#     e_f.edit_contact()

# def del_oper():
#     del_number = int(input('Укажите номер контакта для удаления'))
#     d_f.del_contact(del_number,"spravochnik.txt")

def output_oper():
    o_f.output_contact()

def export_oper():
    list_format = ['txt', 'csv']
    print('Выберите формат файла для экспорта')
    for i, list_format in enumerate(list_format, 1):
        print(f'({i}) -> {list_format}')
    select = int(input('Укажите номер формата: '))
    ex.export_contact(select)

def import_oper():
    print("Контакты добавляются из файл: imp_spr.txt")
    im.import_contact()
    time.sleep(2)
    print("=> Выполненно")

def option():
    main_menu = ['Вывести справочник на экран', 'Создать новый контакт', 'Отредактировать контакт', 'Удалить контакт', 'Экспорт контактов в файл', 'Импорт контактов из файла', 'Выход']
    length = int(len(main_menu))
    print("============Основное меню=============")
    for i, main_menu in enumerate(main_menu, 1):
        print(f'> {i} <  --> {main_menu}')
    print("--------------------------------------")    

    selection = int(input(f'Введите номер операции: '))

    if selection > length:
        print(f"<<<ОШИБКА! Такого номера операции не существует.>>>\n<<<Введите номер операций от 1 до {length} >>>")
        time.sleep(2)    
        option()
    elif selection == 1:
        output_oper()
        time.sleep(3)
        option()

    elif selection == 2:
        add_oper()
        time.sleep(3)    
        option()

    # elif selection == 3:
    #     edit_oper()
    #     option()

    # elif selection == 4:
    #     del_oper
    #     option()

    elif selection == 5:
        export_oper()
        time.sleep(2) 
        option()

    elif selection == 6:
        import_oper()
        option()

    elif selection == 7:
        time.sleep(2)
        print('Программа завершена')

#print(option())