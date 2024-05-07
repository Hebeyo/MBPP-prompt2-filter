def max_difference(test_list):
  temp = []
  for a, b in test_list:
    temp.append(abs(b - a))
  res = max(temp)
  return res
