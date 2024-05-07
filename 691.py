def group_element(test_list):
  res = dict()
  for key in set([ele[1] for ele in test_list]):
    res[key] = [ele[0] for ele in test_list if ele[1] == key]
  return (res)
