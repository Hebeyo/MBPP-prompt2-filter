def dig_let(s):
 l=0
 d=0
 for i in s:
  if (i.isalpha()):
   l+=1
  elif (i.isdigit()):
   d+=1
 return (l,d)
