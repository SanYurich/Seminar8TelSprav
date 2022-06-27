from log_files import log_files as l_f

def output_contact():
    print("==== Телефонный Справочник ====== ")
    sprv = 'spravochnik.txt'
    read_sprv = open(sprv, 'r', encoding = 'utf8')
    for i, line in enumerate(read_sprv, 1):
        strok = line.rstrip('\n')
        print(f'{i} => {strok}')
    read_sprv.close()
    print("================================= ")
    l_f('','',"Вывод справочника на экран")

#output_contact() #TEST
