def count_range_in_list(li, min, max):
	count = 0
	for x in li:
		if min <= x <= max:
			count += 1
	return count
