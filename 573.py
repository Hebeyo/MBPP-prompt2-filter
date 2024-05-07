def unique_product(list_data):
    list_data = list(set(list_data))
    p = 1
    for i in list_data:
        p *= i
    return p
