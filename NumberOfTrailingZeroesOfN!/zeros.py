def zeros(n):
  x = n/5
  return x+zeros(x) if x else 0