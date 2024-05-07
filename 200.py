def position_max(list1):
    max_val = max(list1)
    max_result = []
    for i in range(len(list1)):
        if list1[i] == max_val:
            max_result.append(i)
    return max_result
