def add_lists(test_list, test_tup):
    res = []
    for i in test_tup:
        res.append(i)
    for i in test_list:
        res.append(i)
    return tuple(res)
