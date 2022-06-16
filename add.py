import log as log_case

def new_contact(name, number_phone, status, name_file):
    with open("contact.csv", "a", encoding = 'utf8') as file:
        file.write({name}, {number_phone}, {status})
    print(f"Новый контакт: {name}, {number_phone}, {status}")

    log_case.add_log_str(f"Добавили контакт: {name}, {number_phone}, {status}", "добавление") #логгируем

#new_contact('Вася', '89995556633', 'рабочий')