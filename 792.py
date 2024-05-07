def count_list(input_list):
    count = 0
    for i in input_list:
        if type(i) == list:
            count += 1
    return count
