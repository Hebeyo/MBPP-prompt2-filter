def modified_encode(alist):
    result = []
    count = 1
    for i in range(1, len(alist)):
        if alist[i] == alist[i-1]:
            count += 1
        else:
            if count > 1:
                result.append([count, alist[i-1]])
            else:
                result.append(alist[i-1])
            count = 1
    if count > 1:
        result.append([count, alist[-1]])
    else:
        result.append(alist[-1])
    return result
