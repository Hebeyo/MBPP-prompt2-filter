def max_length(list1):
    max_length = 0
    max_list = []
    for x in list1:
        if len(x) > max_length:
            max_length = len(x)
            max_list = x
    return(max_length, max_list)
