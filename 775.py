def odd_position(nums):
	for i in range(len(nums)):
		if nums[i]%2==i%2:
			continue
		else:
			return False
	return True
