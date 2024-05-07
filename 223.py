def is_majority(arr, n, x):
	count = 0
	for i in range(0, n):
		if (arr[i] == x):
			count += 1
	if (count > n//2):
		return True
	else:
		return False
