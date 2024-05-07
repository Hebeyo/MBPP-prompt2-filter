def colon_tuplex(tuplex,m,n):
  tuplex_colon = list(tuplex)
  tuplex_colon[m].append(n)
  return tuple(tuplex_colon)
