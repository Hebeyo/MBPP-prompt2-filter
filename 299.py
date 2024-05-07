def max_aggregate(stdata):
    temp = {}
    for name, marks in stdata:
        if name not in temp:
            temp[name] = 0
        temp[name] += marks
    return max(temp.items(), key=lambda x: x[1])
