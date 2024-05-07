def get_max_occuring_char(str1):
  max_count = 0
  max_char = ''
  for i in set(str1):
    if str1.count(i) > max_count:
      max_count = str1.count(i)
      max_char = i
  return max_char
