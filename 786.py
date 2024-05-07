def right_insertion(a, x):
    for i in range(len(a)):
        if a[i] >= x:
            return i
    return len(a)
