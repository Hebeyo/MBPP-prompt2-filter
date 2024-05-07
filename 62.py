def smallest_num(xs):
    min = xs[0]
    for i in range(len(xs)):
        if xs[i] < min:
            min = xs[i]
    return min
