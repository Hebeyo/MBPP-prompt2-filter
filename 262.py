def split_two_parts(list1, L):
    list2 = []
    list3 = []
    for i in range(len(list1)):
        if i < L:
            list2.append(list1[i])
        else:
            list3.append(list1[i])
    return list2, list3
