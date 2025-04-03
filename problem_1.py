# Solution 1. Brute Force
def sum_multiples_1():
  total = 0
  for i in range(1000):
    if not i % 3 or not i % 5:
      total += i
  return total

# Solution 2. Efficient solution utilizing arithmetic progression
def calculate_arithmetic_sum(n):
  return (n * (n+1)) // 2

def sum_multiples_2():
  sum_three = 3 * calculate_arithmetic_sum(333)
  sum_five = 5 * calculate_arithmetic_sum(199)
  # Subtract out multiples of both 3 and 5 to avoid double-counting
  # https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle
  sum_fifteen = 15 * calculate_arithmetic_sum(66)

  return sum_three + sum_five - sum_fifteen
