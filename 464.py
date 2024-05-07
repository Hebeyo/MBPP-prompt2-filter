def check_value(dict, n):
    for x in dict.values():
        if x != n:
            return False
    return True
