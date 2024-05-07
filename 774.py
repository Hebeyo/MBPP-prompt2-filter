def check_email(email): 
	import re 
	regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
	if(re.search(regex,email)): 
		return ("Valid Email") 
	else: 
		return ("Invalid Email")
