def find_peak(arr, n): 
	for i in range(n): 
		if i == 0 and arr[i] >= arr[i + 1]: 
			return i 
		if i == n - 1 and arr[i] >= arr[i - 1]: 
			return i 
		if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]: 
			return i 
	return -1
