def anagram_lambda(texts,str):
  result = list(filter(lambda x: (sorted(str) == sorted(x)), texts)) 
  return result
