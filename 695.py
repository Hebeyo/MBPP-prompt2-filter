def check_greater(test_tup1, test_tup2):
  for i in range(len(test_tup1)):
    if test_tup1[i] >= test_tup2[i]:
      return False
  return True
