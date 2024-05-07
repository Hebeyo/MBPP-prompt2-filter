def average_tuple(nums):
    result = []
    for i in range(len(nums[0])):
        sum = 0
        for j in range(len(nums)):
            sum += nums[j][i]
        result.append(sum/len(nums))
    return result
