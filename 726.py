def multiply_elements(test_tup):
  res = []
  for i in range(len(test_tup)-1):
    res.append(test_tup[i] * test_tup[i+1])
  return tuple(res)
