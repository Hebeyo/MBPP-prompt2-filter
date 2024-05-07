def multi_list(rownum,colnum):
  multi_list = []
  for row in range(rownum):
    multi_list.append([])
    for col in range(colnum):
      multi_list[row].append(row*col)
  return multi_list
