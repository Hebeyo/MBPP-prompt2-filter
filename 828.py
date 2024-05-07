def count_alpha_dig_spl(string):
  alphabets=digits = special = 0
  for i in string:
    if(i.isalpha()):
        alphabets = alphabets + 1
    elif(i.isdigit()):
        digits = digits + 1
    else:
        special = special + 1
  return (alphabets,digits,special)
