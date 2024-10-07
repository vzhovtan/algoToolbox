# Input: An integer n.
# Output: N-th Fibonacchi number
def fibnumber(x):
  if x == 0:
    return 0
  if x == 1:
    return 1
  a, b = 0, 1
  for i in range(x-1):
    a, b = b, a + b
  return b

def main():
  n = int(input())
  print(fibnumber(n))

if __name__ == "__main__":
  main()