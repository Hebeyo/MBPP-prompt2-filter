def move_zero(num_list):
    for i in num_list:
        if i == 0:
            num_list.remove(i)
            num_list.append(i)
    return num_list
