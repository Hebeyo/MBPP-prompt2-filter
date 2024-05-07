def max_similar_indices(test_list1, test_list2):
  res = []
  for x, y in zip(test_list1, test_list2):
    res.append((max(x[0], y[0]), max(x[1], y[1])))
  return (res)
