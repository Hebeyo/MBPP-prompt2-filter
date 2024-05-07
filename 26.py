def check_k_elements(test_list, K):
  for tup in test_list:
    for ele in tup:
      if ele != K:
        return False
  return True
