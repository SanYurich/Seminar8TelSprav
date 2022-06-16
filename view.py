import log as log_case

def print_case(data):
   
    with open(data, "r", encoding = 'utf8') as file:
        i = 1
        for line in file:
            print(f"{i} - {line}")
            i += 1
    
    log_case.add_log_str("Вывод списка контактов", "Просмотр")