import view as view_case
import log as log_case
import add as add_case


# def delete_str(number_pfone, number_contact):
#     with open('contact.csv', "w", encoding = 'utf8') as file:
#         temp_list = list(filter(lambda task: task != number_contact))
#         file.write(temp_list)


def delete_str(data, task_del):

    with open(data, "r", encoding = 'utf8') as file:
        temp_list = []
        i = 1
        for line in file:
            if i != task_del: 
                temp_list.append(line)
                
            else:
                log_case.add_logg_str(line[:len(line)-2], "удаление")
            i += 1
       
        with open(data, "w", encoding = 'utf8') as file:
            for tsk in temp_list:
                file.write(tsk)
                
    view_case.print_case(data)