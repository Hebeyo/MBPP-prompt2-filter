def filter_data(students,h,w):
    result = {}
    for k, s in students.items():
        if s[0] >= h and s[1] >= w:
            result[k] = s
    return result
