def remove_elements(list1, list2):
    result = []
    for x in list1:
        if x not in list2:
            result.append(x)
    return result
