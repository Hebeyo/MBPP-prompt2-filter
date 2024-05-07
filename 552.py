def Seq_Linear(seq_nums):
  for i in range(1, len(seq_nums)):
    if seq_nums[i] - seq_nums[i-1] != seq_nums[1] - seq_nums[0]:
      return "Non Linear Sequence"
  return "Linear Sequence"
