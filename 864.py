def palindrome_lambda(texts):
  result = []
  for text in texts:
    if text == "".join(reversed(text)):
      result.append(text)
  return result
