def most_common_elem(s,a):
  d={}
  for i in s:
    if i in d:
      d[i]+=1
    else:
      d[i]=1
  d=sorted(d.items(), key=lambda x: x[1], reverse=True)
  return d[:a]
