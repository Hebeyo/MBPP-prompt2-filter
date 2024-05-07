import re
def remove_extra_char(text1):
  return re.sub(r'\W+', '', text1)
