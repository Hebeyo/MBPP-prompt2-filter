def find_max(test_list):
  res = 0
  for i in test_list:
    for j in i:
      if int(j) > res:
        res = int(j)
  return (res)
