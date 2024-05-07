def max_sum_list(lists):
    max_sum = -1
    max_list = []
    for i in lists:
        if sum(i) > max_sum:
            max_sum = sum(i)
            max_list = i
    return max_list
