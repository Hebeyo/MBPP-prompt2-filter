def maximum_value(test_list):
    res = []
    for i in test_list:
        res.append((i[0], max(i[1])))
    return res
