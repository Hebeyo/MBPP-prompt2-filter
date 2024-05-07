def number_of_substrings(str): 
    str_len = len(str)
    count = 0
    for i in range(str_len):
        for j in range(i, str_len):
            count += 1
    return count
