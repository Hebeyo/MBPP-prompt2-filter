def even_position(nums):
	for i in range(len(nums)):
		if i%2 == 0:
			if nums[i] % 2 != 0:
				return False
		else:
			if nums[i] % 2 == 0:
				return False
	return True
