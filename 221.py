def first_even(nums):
    for i in nums:
        if i % 2 == 0:
            return i
    return -1
