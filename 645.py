def find_k_product(test_list, K):
  res = 1
  for i in range(len(test_list)):
    res *= test_list[i][K]
  return (res)
