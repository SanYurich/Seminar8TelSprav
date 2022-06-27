from log_files import log_files as l_f

def import_contact():
    files = open('imp_spr.txt', 'r', encoding = 'utf8')
    sprv = open('spravochnik.txt', 'a', encoding = 'utf8')
    for i in files:
        sprv.writelines(i)
    l_f('','',"Контакты добавленны из файла")
