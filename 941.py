def count_elim(num):
  count_elim = 0
  for n in num:
    if type(n) == tuple:
        break
    count_elim += 1
  return count_elim
