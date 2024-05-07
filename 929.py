def count_tuplex(tuplex, value):
  count = 0
  for i in tuplex:
    if i == value:
      count += 1
  return count
