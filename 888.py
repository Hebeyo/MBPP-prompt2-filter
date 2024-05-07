def substract_elements(test_tup1, test_tup2):
  res = []
  for tup1, tup2 in zip(test_tup1, test_tup2):
    res.append(tuple(a - b for a, b in zip(tup1, tup2)))
  return tuple(res)
