# Problem 1.
# If we list all the natural numbers below $10 that are multiples of 3
# or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of $3 or $5 below 1000.

# Simple, brute-force solution
def sum_multiples_1():
  total = 0
  for i in range(1000):
    if not i % 3:
      total += i
      continue
    if not i % 5:
      total += i
      continue
  return total

print(sum_multiples())
  
