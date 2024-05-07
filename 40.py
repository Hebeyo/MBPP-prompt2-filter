from collections import Counter
def freq_element(nums):
  result = Counter()
  for i in range(len(nums)):
    for j in range(len(nums[i])):
      result[nums[i][j]] += 1
  return result
