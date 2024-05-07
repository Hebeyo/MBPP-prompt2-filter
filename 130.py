def max_occurrences(nums):
    max_count = 0
    max_item = None
    for i in nums:
        count = nums.count(i)
        if count > max_count:
            max_count = count
            max_item = i
    return (max_item, max_count)
