def group_keyvalue(l):
    result = {}
    for k, v in l:
        if k in result:
            result[k].append(v)
        else:
            result[k] = [v]
    return result
