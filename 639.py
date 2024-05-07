def sample_nam(sample_names):
  sample_names = [name for name in sample_names if name[0].isupper()]
  return len(''.join(sample_names))
