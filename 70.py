def get_equal(Input, k):
    for tuple in Input:
        if len(tuple) != k:
            return 'All tuples do not have same length'
    return 'All tuples have same length'
