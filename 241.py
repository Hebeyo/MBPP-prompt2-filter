def array_3d(m,n,o):
 array_3d = []
 for i in range(o):
  array_3d.append([])
  for j in range(n):
   array_3d[i].append([])
   for k in range(m):
    array_3d[i][j].append('*')
 return array_3d
