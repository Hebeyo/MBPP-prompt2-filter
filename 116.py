def tuple_to_int(nums):
    result = 0
    for i in range(len(nums)):
        result = result*10 + nums[i]
    return result
