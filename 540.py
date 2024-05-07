def find_Diff(arr,n):
    my_dict = {}
    for i in arr:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    max_count = 0
    min_count = n
    for key in my_dict:
        if my_dict[key] > max_count:
            max_count = my_dict[key]
        if my_dict[key] < min_count:
            min_count = my_dict[key]
    return max_count - min_count
