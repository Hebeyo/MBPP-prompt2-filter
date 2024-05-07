def remove_matching_tuple(test_list1, test_list2):
  res = []
  for sub in test_list1:
    if sub not in test_list2:
      res.append(sub)
  return (res)
