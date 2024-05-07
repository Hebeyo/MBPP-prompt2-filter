def max_of_nth(test_list, N):
  max = 0
  for i in test_list:
    if i[N] > max:
      max = i[N]
  return max
