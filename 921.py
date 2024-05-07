def chunk_tuples(test_tup, N):
    res = []
    for i in range(0, len(test_tup), N):
        res.append(test_tup[i : i + N])
    return (res)
