def count_first_elements(test_tup):
    count = 0
    for ele in test_tup:
        if isinstance(ele, tuple):
            break
        count += 1
    return count
