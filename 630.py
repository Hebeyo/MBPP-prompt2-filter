def get_coordinates(test_tup):
  res = []
  def adjac(ele, sub = []): 
    if not ele: 
      res.append(sub) 
    else: 
      for j in range(ele[0] - 1, ele[0] + 2):
        adjac(ele[1:], sub + [j])
  adjac(test_tup)
  return res
