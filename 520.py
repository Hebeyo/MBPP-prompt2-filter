def get_lcm(l):
  lcm = max(l)
  while True:
    if all(lcm % i == 0 for i in l):
      return lcm
    lcm += max(l)
