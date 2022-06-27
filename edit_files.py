# from log_files import log_files as l_f


# def edit_oper():
#     sprv = 'spravochnik.txt'
#     read_sprv = open(sprv, 'r', encoding = 'utf8')
#     temp_file = open('temp.txt', 'w', encoding = 'utf8')
#     for i, line in enumerate(read_sprv, 1):
#         strok = line.rstrip('\n')
#         print(f'{i} => {strok}')   
#     # read_sprv.close()
#     search = int(input('Укажите номер контакта, который будем редактировать:'))
#     for i, line in enumerate(read_sprv, 1):
#         if i == search:
#             name = input("Укажите новое название контакта")
#             number = input("Укажите новый номер контакта")
#             temp_file.write(f"{name}, {number}\n")
#         else:
#             temp_file.append(line)

    


    # def delete_str(data, task_del):

    # with open(data, "r", encoding = 'utf8') as file:
    #     temp_list = []
    #     i = 1
    #     for line in file:
    #         if i != task_del: 
    #             temp_list.append(line)
                
    #         else:
    #             log_case.add_logg_str(line[:len(line)-2], "удаление")
    #         i += 1
       
    #     with open(data, "w", encoding = 'utf8') as file:
    #         for tsk in temp_list:
    #             file.write(tsk)
                
    # view_case.print_case(data)

# edit_oper()

    # with open('contact.csv', "w", encoding = 'utf8') as file:
    #     temp_list = list(filter(lambda task: task != number_contact))
    #     file.write(temp_list)



# import os

# def edit():
#     found = False
#     search = input ('Введите искомое описание: ')
#     new_coment = input('Введите новое количество: ')
#     sprv_file = open('spravochnik.txt', 'r', encoding = 'utf8')
#     temp_file = open('temp.txt', "w", encoding = 'utf8')
#     descr = sprv_file.readline()
#     while descr != '':
#         qty = sprv_file.readline()
#         descr = descr.rstrip('\n')
#         if descr == search:
#             temp_file.write(f'{descr}\n')
#             temp_file.write(f'{new_coment}\n')
#             found = True
#         else:
#             temp_file.write(f'{descr}\n')
#             temp_file.write(f'{qty}\n')
#         descr = sprv_file.readline()
#     sprv_file.close()
#     temp_file.close()
#     os.remove('spravochnik.txt')
#     os.rename('temp.txt','spravochnik.txt')
#     if found:
#         print('Файл обновлен')
#     else:
#         print("Это значение в файле не найдено")
    
# edit()


