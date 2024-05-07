def remove(list):
    new_list = []
    for i in list:
        new_list.append(''.join([j for j in i if not j.isdigit()]))
    return new_list
