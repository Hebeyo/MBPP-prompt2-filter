def sort_sublists(input_list):
    result = []
    for x in input_list:
        result.append(sorted(x, key = lambda x:x[0]))
    return result
