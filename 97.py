def frequency_lists(list1):
    dic_data = {}
    for sublist in list1:
        for num in sublist:
            if num in dic_data.keys():
                dic_data[num] += 1
            else:
                key = num
                value = 1
                dic_data[key] = value
    return dic_data
