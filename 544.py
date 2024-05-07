def flatten_tuple(test_list):
  res = ''
  for tup in test_list:
    for idx in tup:
      res += idx + ' '
  return res[:-1]
