def min_product_tuple(list1):
    result_min = float('inf')
    for x, y in list1:
        result_min = min(result_min, abs(x * y))
    return result_min
