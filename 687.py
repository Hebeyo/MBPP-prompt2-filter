def recur_gcd(a, b):
	if a == 0:
		return b
	elif b == 0:
		return a
	elif a == b:
		return a
	elif a > b:
		return recur_gcd(a-b, b)
	else:
		return recur_gcd(a, b-a)
