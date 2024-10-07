# Input: An integer n.
# Output: the last digit of sum F0 + F1 ... + Fn
def lastdigsum(x):
  if x == 0:
    return 0
  summ = 0
  a, b = 0, 1
  for i in range(x-1):
    a, b = b, a + b
    summ += a
  return (summ + b) % 10

def main():
  n = int(input())
  if n < 60:
    print(lastdigsum(n))
  else:
    print(lastdigsum(n % 60))

if __name__ == "__main__":
  main()