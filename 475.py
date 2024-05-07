def sort_counter(dict1):
    list1 = []
    for key, value in dict1.items():
        list1.append((value,key))
    list1.sort(reverse=True)
    return [(i[1],i[0]) for i in list1]
