def remove_tuples(test_list, K):
  res = []
  for ele in test_list:
    if len(ele) != K:
      res.append(ele)
  return (res)
