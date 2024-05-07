def tuple_to_dict(test_tup):
  res = {test_tup[idx]: test_tup[idx + 1] for idx in range(0, len(test_tup), 2)}
  return (res)
