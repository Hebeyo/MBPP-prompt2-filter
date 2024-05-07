def sort_sublists(list1):
    for i in range(len(list1)):
        list1[i] = sorted(list1[i])
    return list1
