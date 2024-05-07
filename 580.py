def extract_even(test_tuple):
    res = ()
    for ele in test_tuple:
        if isinstance(ele, tuple):
            res += (extract_even(ele), )
        elif ele % 2 == 0:
            res += (ele, )
    return res
