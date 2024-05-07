def convert_list_dictionary(l1, l2, l3):
    result = []
    for i in range(len(l1)):
        result.append({l1[i]: {l2[i]: l3[i]}})
    return result
