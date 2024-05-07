def extract_rear(test_tuple):
    res = []
    for sub in test_tuple:
        res.append(sub[len(sub) - 1])
    return (res)
