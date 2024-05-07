def sort_numeric_strings(nums_str):
    for i in range(len(nums_str)):
        nums_str[i] = int(nums_str[i])
    nums_str.sort()
    return nums_str
