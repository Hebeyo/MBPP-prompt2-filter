def freq_count(list1):
  freq_count= {}
  for i in list1:
    if i in freq_count:
      freq_count[i] += 1
    else:
      freq_count[i] = 1
  return freq_count
