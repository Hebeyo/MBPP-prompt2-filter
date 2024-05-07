def find_exponentio(test_tup1, test_tup2):
  res = []
  for ele1, ele2 in zip(test_tup1, test_tup2):
    res.append(ele1 ** ele2)
  return tuple(res)
