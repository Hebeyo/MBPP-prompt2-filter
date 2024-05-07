def comb_sort(nums):
    n = len(nums)
    gap = n
    swapped = True
    while gap != 1 or swapped:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1
        swapped = False
        i = 0
        while i + gap < n:
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                swapped = True
            i += 1
    return nums
