def sort_mixed_list(mixed_list):
    int_part = []
    str_part = []
    for i in mixed_list:
        if type(i) is int:
            int_part.append(i)
        else:
            str_part.append(i)
    int_part.sort()
    str_part.sort()
    return int_part + str_part
