from datetime import datetime as dat


def log_files(name, number, comment):
    time = dat.today().strftime("%H:%M:%S  %d.%m.%Y")
    with open ('logger.txt', 'a',encoding = 'utf8') as log_data:
        log_data.write(f'{time}, - {name}, {number}, {comment}\n')

#log_files('Петя','89985','личный') #TEST
