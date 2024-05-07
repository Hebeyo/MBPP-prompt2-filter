def find_tuples(test_list, K):
  res = []
  for sub in test_list:
    if all(ele % K == 0 for ele in sub):
      res.append(sub)
  return (str(res))
