def large_product(nums1, nums2, N):
    result = []
    for x in nums1:
        for y in nums2:
            result.append(x*y)
    result = sorted(result, reverse=True)[:N]
    return result
