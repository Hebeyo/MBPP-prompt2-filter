def remove_tuple(test_list):
  res = []
  for sub in test_list:
    if not all(ele == None for ele in sub):
      res.append(sub)
  return (str(res))
