def intersection_nested_lists(l1, l2):
    result = []
    for lst in l2:
        temp = []
        for n in lst:
            if n in l1:
                temp.append(n)
        result.append(temp)
    return result
