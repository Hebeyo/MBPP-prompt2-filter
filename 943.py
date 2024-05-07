def combine_lists(num1,num2):
  from heapq import merge
  return list(merge(num1, num2))
