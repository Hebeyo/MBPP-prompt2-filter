def max_sum(tri, n): 
	for i in range(1, n): 
		for j in range(i+1): 
			if j == 0: 
				tri[i][j] = tri[i][j] + tri[i-1][j] 
			elif j == i: 
				tri[i][j] = tri[i][j] + tri[i-1][j-1] 
			else: 
				tri[i][j] = tri[i][j] + max(tri[i-1][j-1], tri[i-1][j]) 
	return (max(tri[n-1]))
