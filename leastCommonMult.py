# Input: An integer a and b
# Output: The least common multiple of a and b

import math

def gcd(a, b):
  while (b):
    a, b = b, a % b
  return a

def lcm(a, b):
  lcm = (a * b) // gcd(a, b)
  return lcm

def main():
  a, b = map(int, input().split(" "))
  print(lcm(a, b))
  #print(math.lcm(a, b))

if __name__ == "__main__":
  main()