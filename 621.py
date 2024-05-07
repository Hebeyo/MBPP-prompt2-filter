def increment_numerics(test_list, K):
  res = []
  for ele in test_list:
    if ele.isdigit():
      res.append(str(int(ele) + K))
    else:
      res.append(ele)
  return res
