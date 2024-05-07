def freq_element(test_tup):
  res = {}
  for ele in test_tup:
    if ele in res:
      res[ele] += 1
    else:
      res[ele] = 1
  return (str(res))
