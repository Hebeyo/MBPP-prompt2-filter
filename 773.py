def occurance_substring(text,pattern):
  for i in range(len(text)-len(pattern)+1):
    if text[i:i+len(pattern)]==pattern:
      return (pattern, i, i+len(pattern))
  return None
