def extract_column(list1, n):
   result = []
   for i in list1:
      result.append(i.pop(n))
   return result
