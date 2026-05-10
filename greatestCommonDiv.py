# Input: An integer a and b
# Output: The greatest common divisor of a and b

import math

def gcd(a, b):
  while (b):
    a, b = b, a % b
  return abs(a)

def main():
  a, b = map(int, input().split(" "))
  print(gcd(a, b))
  # print(math.gcd(a, b))

if __name__ == "__main__":
  main()