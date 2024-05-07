def find_substring(str1, sub_str):
  for s in str1:
    if sub_str in s:
      return True
  return False
