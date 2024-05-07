def index_minimum(test_list):
  res = test_list[0][0]
  min_val = test_list[0][1]
  for i in range(1, len(test_list)):
    if test_list[i][1] < min_val:
      min_val = test_list[i][1]
      res = test_list[i][0]
  return (res)
