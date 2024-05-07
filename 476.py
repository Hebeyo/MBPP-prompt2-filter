def big_sum(nums):
    sum = 0
    for i in range(len(nums)):
        if i == 0:
            max = nums[i]
            min = nums[i]
        else:
            if nums[i] > max:
                max = nums[i]
            if nums[i] < min:
                min = nums[i]
    sum = max + min
    return sum
