def get_unique(test_list):
  res = {}
  for sub in test_list:
    if sub[1] in res:
      res[sub[1]].append(sub[0])
    else:
      res[sub[1]] = [sub[0]]
  res_dict = {}
  for key in res:
    res_dict[key] = len(set(res[key]))
  return (str(res_dict))
