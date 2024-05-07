def get_gcd(l):
  gcd = l[0]
  for i in range(1, len(l)):
    num1 = gcd
    num2 = l[i]
    while(num2):
      num1, num2 = num2, num1 % num2
    gcd = num1
  return gcd
