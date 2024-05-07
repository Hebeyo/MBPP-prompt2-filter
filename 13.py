from collections import Counter
def count_common(words):
  result = []
  word_counts = Counter(words)
  top_four = word_counts.most_common(4)
  for i in top_four:
    result.append(i)
  return result
