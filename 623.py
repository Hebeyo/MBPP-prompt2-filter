def nth_nums(nums,n):
 nth_nums = []
 for i in range(len(nums)):
  nth_nums.append(nums[i]**n)
 return nth_nums
