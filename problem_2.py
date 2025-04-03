# Solution 1. Brute Force
def sum_fibonacci():
  a, b = 1, 2
  total = 0
  while a < 4_000_000:
    if not a % 2:
      total += a
    a, b = b, a+b
  return total
