def num_comm_div(x, y):
  i = 1
  gcd = 0
  while(i <= x and i <= y):
    if(x % i == 0 and y % i == 0):
      gcd = i;
    i += 1
  result = 0
  z = int(gcd**0.5)
  i = 1
  while(i <= z):
    if(gcd % i == 0):
      result += 2 
      if(i == gcd/i):
        result -= 1
    i += 1
  return result
