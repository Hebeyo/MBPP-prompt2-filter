def max_val(listval):
    maxval = 0
    for i in listval:
        if isinstance(i, int):
            if i > maxval:
                maxval = i
    return maxval
