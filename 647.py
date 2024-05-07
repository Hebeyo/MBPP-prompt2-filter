def split_upperstring(text):
  res = []
  start = 0
  for i in range(1, len(text)):
    if text[i].isupper():
      res.append(text[start:i])
      start = i
  res.append(text[start:])
  return res
