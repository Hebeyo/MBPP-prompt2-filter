def most_occurrences(test_list):
  temp = {}
  for sub in test_list:
    for wrd in sub.split():
      if wrd in temp:
        temp[wrd] += 1
      else:
        temp[wrd] = 1
  res = max(temp, key=temp.get)
  return (str(res))
