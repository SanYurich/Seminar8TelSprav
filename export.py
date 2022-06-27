from log_files import log_files as l_f

def export_contact(select):
    with open ('spravochnik.txt' ,'r', encoding = 'utf8') as spr_file:
        if select == 1:
            with open ('exp_contact.txt' ,'w', encoding = 'utf8') as txt_file:
                for i in spr_file:
                    txt_file.write(i)
        elif select == 2:
            with open ('exp_contact.csv' ,'w', encoding = 'utf8') as txt_file:
                for i in spr_file:
                    txt_file.write(i)
        print("Название файла: exp_contact")

    l_f('','',"Телефонный справочник экспортирован")