def basesnum_coresspondingnum(bases_num,index):
  result = []
  for i in range(len(bases_num)):
    result.append(bases_num[i]**index[i])
  return result
