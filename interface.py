import add as add_case
import delete as del_case
import log as log_case
import view as view_case


def print_spisok_phone(data):
    print("<Cписок телефонных контактов:")
    view_case.print_case(data)

def delete_contact(data):
    print_spisok_phone(data)
    cont_del = int(input("Укажите номер удаляемого контакта: "))
    del_case.delete_str(data, cont_del) 
    print("Обновленный справочник:")
    print_spisok_phone(data)

def add_unit_case():
    name = input(f"Введите Имя контакта: ")
    number_phone = input(f"Теперь телефонный номер: ")
    status = input(f"Выберите статус: ") # Нужна функция выбора статусов (личный, домашний, рабочий)
    add_case.new_contact({name}, {number_phone}, {status}, "contact_log.txt")

def main_menu():

    list_operation = ['<<Основное меню>>','Телефонный справочник', 'Добавление нового контакта', 'Удаление контакта', 'Выход']

    for i, list_operation in enumerate(list_operation, 0):
        print(i, list_operation)

    number = int(input("Укажите номер операции: "))

    if number == 1:
        print_spisok_phone("task_log.txt")
        main_menu()
    elif number == 2:
        add_unit_case()
        main_menu()
    elif number == 3:
        delete_contact("task_log.txt")
        main_menu()
    elif number == 4:
        print('<Программа завершена>')