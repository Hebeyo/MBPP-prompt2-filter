def extract_string(str, l):
    result = []
    for e in str:
        if len(e) == l:
            result.append(e)
    return result
