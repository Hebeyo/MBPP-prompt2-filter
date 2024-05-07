def union_elements(test_tup1, test_tup2):
  res = test_tup1 + test_tup2
  res = tuple(set(res))
  return (res)
