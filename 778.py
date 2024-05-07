def pack_consecutive_duplicates(list1):
    res = []
    for i in range(len(list1)):
        if i == 0 or list1[i] != list1[i-1]:
            res.append([list1[i]])
        else:
            res[-1].append(list1[i])
    return res
