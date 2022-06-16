from datetime import datetime as data_time


def add_log_str(name, number_phone, status, operation):
    time = data_time.now()
    with open("log.txt", "a", encoding = 'utf8') as file:
        file.write(f"{name}; {number_phone}; {status}; {operation}; {time} \n")
    return