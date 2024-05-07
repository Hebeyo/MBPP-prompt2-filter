def dict_filter(dict,n):
    result = {}
    for key, value in dict.items():
        if value >= n:
            result[key] = value
    return result
