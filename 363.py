def add_K_element(test_list, K):
  res = []
  for sub in test_list:
    res.append(tuple(j + K for j in sub))
  return res
