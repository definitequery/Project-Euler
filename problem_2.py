#!/usr/bin/python3
LIMIT = 4_000_000

def calculate_fibonacci_sum(n):
  total = 0
  a, b = 0, 1
  while a < n:
    if (a % 2 == 0):
      total += a
    a, b = b, a + b
  return total

if __name__ == "__main__":
  result = calculate_fibonacci_sum(LIMIT)
  print(f'The sum of all even numbers in the Fibonacci sequence up to {LIMIT} is {result}')

# Solution Time Complexity:
# The time complexity of the fibonacci() function is O(log(n)), where n is the limit (4,000,000).
# This is because the Fibonacci sequence grows exponentially, and the number of Fibonacci numbers
# less than n is proportional to log(n) in terms of the number of iterations needed to generate them.

# In each iteration, we perform a constant amount of work (checking if the number is even and appending
# it to the result list). Therefore, the overall time complexity for calculating the sum in
# calculate_fibonacci_sum() is also O(log(n)).

# Solution Space Complexity:
# The fibonacci() function generates even Fibonacci numbers less than n and appends them to a list.
# Since the number of Fibonacci numbers less than n is proportional to log(n), the space complexity
# of this function is O(log(n))

# The calculate_fibonacci_sum() function only calls fibonacci(), which generates the O(log(n)) list.
# The total variable is O(1) space. 