def check_smaller(test_tup1, test_tup2):
  res = True
  for i in range(len(test_tup1)):
    if test_tup1[i] <= test_tup2[i]:
      res = False
  return res
