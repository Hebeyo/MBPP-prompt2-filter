def check_occurences(test_list):
  res = {}
  for i in test_list:
    if tuple(sorted(i)) in res:
      res[tuple(sorted(i))] += 1
    else:
      res[tuple(sorted(i))] = 1
  return res
