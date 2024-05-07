def check_distinct(test_tup):
  temp = set()
  for ele in test_tup:
    if ele in temp:
      return False
    temp.add(ele)
  return True
