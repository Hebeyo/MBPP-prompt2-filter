def removezero_ip(ip):
  ip = ip.split('.')
  for i in range(len(ip)):
    ip[i] = str(int(ip[i]))
  return '.'.join(ip)
