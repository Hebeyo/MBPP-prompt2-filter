def min_k(test_list, K):
  res = []
  for i in range(K):
    res.append(sorted(test_list, key = lambda x: x[1])[i])
  return (res)
