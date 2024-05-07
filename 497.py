def surfacearea_cone(r,h):
  import math
  l = math.sqrt(r * r + h * h)
  SA = math.pi * r * (r + l)
  return SA
