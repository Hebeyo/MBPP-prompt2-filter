def largest_palindrome(A, n) : 
	A.sort() 
	for i in range(n - 1, -1, -1) : 
		if str(A[i]) == str(A[i])[::-1] : 
			return A[i] 
	return -1
