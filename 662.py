def sorted_dict(dict1):
  sorted_dict = {x: sorted(dict1[x]) for x in dict1}
  return sorted_dict
