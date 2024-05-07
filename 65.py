def recursive_list_sum(data_list):
	sum = 0
	for element in data_list:
		if type(element) == type([]):
			sum = sum + recursive_list_sum(element)
		else:
			sum = sum + element
	return sum
