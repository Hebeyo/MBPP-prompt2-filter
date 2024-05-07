def count_reverse_pairs(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for idxn in range(idx, len(test_list)):
      if test_list[idxn] == str(''.join(list(reversed(test_list[idx])))):
        res += 1
  return str(res)
