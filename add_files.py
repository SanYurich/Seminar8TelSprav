from log_files import log_files as l_f

def add_contact(name, number, file):
    with open(file, "a", encoding = 'utf8') as sprav:
        sprav.write(f"{name}, {number}\n")
    l_f(name, number, "Добавлен новый контакт")
    print(f'>> Добавлен новый контакт: {name}, {number}')
