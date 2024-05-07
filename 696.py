def zip_list(list1,list2):
  result = []
  for x,y in zip(list1,list2):
    result.append(x+y)
  return result
