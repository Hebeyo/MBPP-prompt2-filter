def cummulative_sum(test_list):
    res = 0
    for ele in test_list:
        res += sum(ele)
    return (res)
