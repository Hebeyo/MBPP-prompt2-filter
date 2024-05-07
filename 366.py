def adjacent_num_product(list_nums):
    max_product = 0
    for i in range(len(list_nums)-1):
        prod = list_nums[i] * list_nums[i+1]
        if prod > max_product:
            max_product = prod
    return max_product
