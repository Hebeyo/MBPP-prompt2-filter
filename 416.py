def breakSum(n): 
	if n == 0: 
		return 0
	return max(n, breakSum(int(n/2)) + breakSum(int(n/3)) + breakSum(int(n/4)) )
