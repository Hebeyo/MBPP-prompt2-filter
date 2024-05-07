def min_length_list(input_list):
    min_length = len(input_list[0])
    min_list = input_list[0]
    for i in input_list:
        if len(i)<min_length:
            min_length = len(i)
            min_list = i
    return(min_length, min_list)
