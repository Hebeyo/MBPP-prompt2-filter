def substract_elements(test_tup1, test_tup2):
    res = ()
    for i in range(len(test_tup1)):
        res += (test_tup1[i] - test_tup2[i]),
    return res